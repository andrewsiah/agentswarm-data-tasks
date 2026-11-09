"""Parse one reward string; see SPEC.md."""
from decimal import Decimal
import re

CURRENCIES_CASH = {"USD", "EUR", "GBP", "CAD", "AUD", "CHF", "JPY", "INR"}
CURRENCIES_CRYPTO = {"USDC", "USDT", "ETH", "BTC", "SOL"}
CURRENCIES_POINTS = {"XTR", "POINTS"}
CURRENCIES_BALANCE = {"CREDITS"}

SYMBOL_MAP = {
    "$": ("USD", "cash"),
    "€": ("EUR", "cash"),
    "£": ("GBP", "cash"),
}

CURRENCY_MAP = {}
for c in CURRENCIES_CASH:
    CURRENCY_MAP[c] = ("cash", c)
for c in CURRENCY_CRYPTO:
    CURRENCY_MAP[c] = ("crypto", c)
for c in CURRENCY_POINTS:
    CURRENCY_MAP[c] = ("points", c)
for c in CURRENCY_BALANCE:
    CURRENCY_MAP[c] = ("site-balance", "CREDITS")

UNKNOWN = {"amount": None, "currency": None, "kind": "unknown"}


def _parse_amount_token(s: str):
    if not s or not s.isascii():
        return None
    if "," in s:
        int_part = s.split(".", 1)[0]
        groups = int_part.split(",")
        if not groups[0] or len(groups[0]) > 3 or not groups[0].isdigit():
            return None
        for g in groups[1:]:
            if len(g) != 3 or not g.isdigit():
                return None
        if "." in s:
            frac = s.split(".", 1)[1]
            if not frac or "." in frac or "," in frac or not frac.isdigit():
                return None
    else:
        if "." in s:
            parts = s.split(".")
            if len(parts) != 2 or not parts[0] or not parts[1]:
                return None
            if not (parts[0].isdigit() and parts[1].isdigit()):
                return None
        else:
            if not s.isdigit():
                return None
    try:
        dec = Decimal(s.replace(",", ""))
        if not dec.is_finite() or dec < 0:
            return None
        return dec
    except Exception:
        return None


def parse_reward(text: str) -> dict:
    if not isinstance(text, str) or "\x00" in text:
        return dict(UNKNOWN)

    tokens_raw = text.strip().split()
    if not tokens_raw:
        return dict(UNKNOWN)
    s = " ".join(tokens_raw)

    m_pref = re.match(r"^(?:reward|bounty)\s*:\s*(.*)$", s, flags=re.IGNORECASE)
    if m_pref:
        s = m_pref.group(1).strip()

    m_qual = re.match(r"^(?:up\s+to|approximately|~)\s*(.*)$", s, flags=re.IGNORECASE)
    if m_qual:
        s = m_qual.group(1).strip()

    m_fix = re.search(r"\s*\(\s*test\s+fixture\s*\)$", s, flags=re.IGNORECASE)
    if m_fix:
        tail = s[m_fix.start():].strip().lower()
        if tail != "(test fixture)":
            return dict(UNKNOWN)
        s = s[:m_fix.start()].strip()

    force_site_balance = False
    for pat in (
        r"\s+gross\s+of\s+site\s+balance$",
        r"\s+\(site\s+balance\)$",
        r"\s+site\s+balance$",
    ):
        m_sb = re.search(pat, s, flags=re.IGNORECASE)
        if m_sb:
            force_site_balance = True
            s = s[:m_sb.start()].strip()
            break

    if not s:
        return dict(UNKNOWN)

    parts = s.split(" ")
    sym = None
    amt_str = None
    code = None

    if len(parts) == 1:
        p0 = parts[0]
        if p0 and p0[0] in SYMBOL_MAP:
            sym = p0[0]
            amt_str = p0[1:]
        else:
            return dict(UNKNOWN)
    elif len(parts) == 2:
        p0, p1 = parts[0], parts[1]
        if p0 in SYMBOL_MAP:
            sym = p0
            amt_str = p1
        elif p0.upper() in CURRENCY_MAP:
            code = p0.upper()
            amt_str = p1
        elif p1.upper() in CURRENCY_MAP:
            code = p1.upper()
            amt_str = p0
        else:
            return dict(UNKNOWN)
    elif len(parts) == 3:
        p0, p1, p2 = parts[0], parts[1], parts[2]
        if p0.upper() in CURRENCY_MAP and p2 in SYMBOL_MAP:
            code = p0.upper()
            amt_str = p1
            sym = p2
        elif p0 in SYMBOL_MAP and p2.upper() in CURRENCY_MAP:
            sym = p0
            amt_str = p1
            code = p2.upper()
        else:
            return dict(UNKNOWN)
    else:
        return dict(UNKNOWN)

    dec = _parse_amount_token(amt_str)
    if dec is None:
        return dict(UNKNOWN)

    resolved_curr = None
    resolved_kind = None

    if sym and not code:
        resolved_curr, resolved_kind = SYMBOL_MAP[sym]
    elif code and not sym:
        resolved_kind, resolved_curr = CURRENCY_MAP[code]
    elif sym and code:
        kind_c, curr_c = CURRENCY_MAP[code]
        if sym == "$" and curr_c in ("USD", "USDC", "USDT"):
            resolved_curr = curr_c
            resolved_kind = kind_c
        elif sym == "€" and curr_c == "EUR":
            resolved_curr = "EUR"
            resolved_kind = "cash"
        elif sym == "£" and curr_c == "GBP":
            resolved_curr = "GBP"
            resolved_kind = "cash"
        else:
            return dict(UNKNOWN)
    else:
        return dict(UNKNOWN)

    if force_site_balance:
        resolved_kind = "site-balance"

    return {
        "amount": dec,
        "currency": resolved_curr,
        "kind": resolved_kind,
    }
