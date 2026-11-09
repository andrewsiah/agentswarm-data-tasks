"""Parse one reward string; see SPEC.md."""
from decimal import Decimal
import re

# Mapping for currencies and kinds
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
for c in CURRENCIES_CRYPTO:
    CURRENCY_MAP[c] = ("crypto", c)
for c in CURRENCIES_POINTS:
    if c == "POINTS":
        CURRENCY_MAP[c] = ("points", "POINTS")
    else:
        CURRENCY_MAP[c] = ("points", c)
for c in CURRENCIES_BALANCE:
    CURRENCY_MAP[c] = ("site-balance", "CREDITS")


def parse_reward(text):
    if not isinstance(text, str):
        return {"amount": None, "currency": None, "kind": "unknown"}

    t = text.strip()
    # Case insensitive matching
    t_lower = t.lower()

    # Optional prefix: reward: or bounty:
    prefix_pattern = r"^(?:reward|bounty)\s*:\s*"
    t_lower = re.sub(prefix_pattern, "", t_lower, flags=re.IGNORECASE)
    t = re.sub(prefix_pattern, "", t, flags=re.IGNORECASE)

    # Optional suffix: literal (test fixture) at the very end
    if t_lower.endswith("(test fixture)"):
        t_lower = t_lower[:-13].strip()
        t = t[:-13].strip()

    # Optional suffix: site balance, (site balance) or gross of site balance
    force_site_balance = False
    site_balance_patterns = [
        r"\bgr[oó]ss\s+of\s+site\s+balance\b",
        r"\b\(site\s+balance\)\b",
        r"\bsite\s+balance\b",
    ]
    for pat in site_balance_patterns:
        match = re.search(pat, t_lower)
        if match:
            force_site_balance = True
            # Remove the suffix from strings
            t_lower = (t_lower[:match.start()] + " " + t_lower[match.end():]).strip()
            t = (t[:match.start()] + " " + t[match.end():]).strip()
            break

    # Optional prefix/qualifier: up to, approximately, ~
    qualifier_pattern = r"^(?:up\s+to|approximately|~)\s*"
    t_lower = re.sub(qualifier_pattern, "", t_lower, flags=re.IGNORECASE)
    t = re.sub(qualifier_pattern, "", t, flags=re.IGNORECASE)

    t = t.strip()
    t_lower = t.lower()

    if not t:
        return {"amount": None, "currency": None, "kind": "unknown"}

    # Now we expect exactly one amount and currency in either order.
    # Symbols $, €, £ may appear before the amount.
    # Amount format: ASCII digits, optionally properly grouped by commas in groups of three, optionally followed by dot and one or more digits.
    # No sign, exponent, decimal comma, range or multiple amounts.

    # Let's tokenize by whitespace
    tokens = t.split()
    if not tokens or len(tokens) > 3:
        return {"amount": None, "currency": None, "kind": "unknown"}

    # Helper to validate number format
    def parse_amount_str(s):
        # s might have a leading symbol like $, €, £
        sym = None
        if s and s[0] in SYMBOL_MAP:
            sym = s[0]
            s = s[1:]
        elif s.upper() in {"USD", "EUR", "GBP", "CAD", "AUD", "CHF", "JPY", "INR", "USDC", "USDT", "ETH", "BTC", "SOL", "XTR", "POINTS", "CREDITS"}:
            return None, None

        # Validate digits and commas/dots
        # Proper grouping by commas in groups of three: e.g. 1,000 or 12,345,678 or 450 or 0.05
        # No decimal comma, no sign, no exponent
        # Regex for valid amount:
        # ^(0|[1-9][0-9]{0,2}(,[0-9]{3})*)([.][0-9]+)?$ or ^([0-9]+([.][0-9]+)?)$ where commas are correctly placed.
        # Let's write a strict regex for comma grouping:
        # Entire number part without symbol:
        pattern = r"^(?:0|[1-9][0-9]{0,2}(?:,[0-9]{3})*)(?:\.[0-9]+)?$"
        if not re.match(pattern, s):
            # Also allow simple unformatted digits like 05 or 0.05
            pattern_simple = r"^(?:0|[0-9]+)(?:\.[0-9]+)?$"
            if not re.match(pattern_simple, s):
                return None, None
            else:
                # Check if commas are used, they must be in groups of three
                if "," in s:
                    parts = s.split(".")[0]
                    groups = parts.split(",")
                    if len(groups[0]) > 3 or any(len(g) != 3 for g in groups[1:]):
                        return None, None
        else:
            # If matched first pattern, commas are already verified by regex (groups of three after 1-3 digits, or single 0)
            pass

        try:
            dec = Decimal(s.replace(",", ""))
            if not dec.is_finite() or dec < 0:
                return None, None
            return dec, sym
        except Exception:
            return None, None

    # Analyze tokens
    amount_val = None
    symbol_found = None
    curr_token = None

    # Clean tokens and filter empty
    clean_tokens = [tk for tk in tokens if tk]
    if len(clean_tokens) == 1:
        # Could be symbol + amount (e.g. €20) or amount alone (symbol alone implies USD/EUR/GBP)
        tok = clean_tokens[0]
        sym = None
        if tok[0] in SYMBOL_MAP:
            sym = tok[0]
            num_part = tok[1:]
        else:
            num_part = tok

        dec, s_sym = parse_amount_str(num_part)
        if dec is not None:
            amount_val = dec
            symbol_found = sym or s_sym
            curr_token = None
        else:
            return {"amount": None, "currency": None, "kind": "unknown"}

    elif len(clean_tokens) == 2:
        # Either [amount, currency], [currency, amount], [symbol+amount, currency], [symbol, amount]
        tok0, tok1 = clean_tokens[0], clean_tokens[1]

        # Check if tok0 is symbol alone
        if tok0 in SYMBOL_MAP:
            dec, _ = parse_amount_str(tok1)
            if dec is not None:
                amount_val = dec
                symbol_found = tok0
                curr_token = None
            else:
                return {"amount": None, "currency": None, "kind": "unknown"}
        else:
            # Try tok0 as amount (maybe with symbol), tok1 as currency
            dec0, sym0 = parse_amount_str(tok0)
            curr1_upper = tok1.upper()

            if dec0 is not None and curr1_upper in CURRENCY_MAP:
                amount_val = dec0
                symbol_found = sym0
                curr_token = curr1_upper
            else:
                # Try tok0 as currency, tok1 as amount (maybe with symbol)
                curr0_upper = tok0.upper()
                dec1, sym1 = parse_amount_str(tok1)
                if dec1 is not None and curr0_upper in CURRENCY_MAP:
                    amount_val = dec1
                    symbol_found = sym1
                    curr_token = curr0_upper
                else:
                    return {"amount": None, "currency": None, "kind": "unknown"}
    else:
        return {"amount": None, "currency": None, "kind": "unknown"}

    # Resolve currency and kind
    # Rules:
    # - Symbols alone imply USD/EUR/GBP (matching SYMBOL_MAP)
    # - A symbol plus its matching cash code is allowed.
    # - $ plus USDC/USDT is also allowed (e.g. $450 USDC);
    # - other symbol/code conflicts are unknown.
    # - Currencies: USD/EUR/GBP/CAD/AUD/CHF/JPY/INR are cash;
    #   USDC/USDT/ETH/BTC/SOL are crypto;
    #   XTR and points are points;
    #   credits is site-balance.

    resolved_currency = None
    resolved_kind = None

    if curr_token is None:
        if symbol_found in SYMBOL_MAP:
            resolved_currency, resolved_kind = SYMBOL_MAP[symbol_found]
        else:
            # No currency, no symbol -> unknown
            return {"amount": None, "currency": None, "kind": "unknown"}
    else:
        kind_mapped, canonical_curr = CURRENCY_MAP[curr_token]
        if symbol_found is not None:
            # Check symbol/code compatibility
            if symbol_found == "$":
                if canonical_curr in {"USD", "USDC", "USDT"}:
                    resolved_currency = canonical_curr
                    resolved_kind = kind_mapped
                    if canonical_curr in {"USDC", "USDT"}:
                        resolved_kind = "crypto"
                else:
                    return {"amount": None, "currency": None, "kind": "unknown"}
            elif symbol_found == "€":
                if canonical_curr == "EUR":
                    resolved_currency = "EUR"
                    resolved_kind = "cash"
                else:
                    return {"amount": None, "currency": None, "kind": "unknown"}
            elif symbol_found == "£":
                if canonical_curr == "GBP":
                    resolved_currency = "GBP"
                    resolved_kind = "cash"
                else:
                    return {"amount": None, "currency": None, "kind": "unknown"}
            else:
                return {"amount": None, "currency": None, "kind": "unknown"}
        else:
            resolved_currency = canonical_curr
            resolved_kind = kind_mapped

    if force_site_balance:
        resolved_kind = "site-balance"

    if resolved_currency is None or resolved_kind is None:
        return {"amount": None, "currency": None, "kind": "unknown"}

    return {
        "amount": amount_val,
        "currency": resolved_currency,
        "kind": resolved_kind,
    }
