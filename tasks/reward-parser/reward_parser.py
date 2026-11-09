"""Parse one reward string; see SPEC.md."""

import re
from decimal import Decimal

CURRENCY_KINDS = {
    **dict.fromkeys(("USD", "EUR", "GBP", "CAD", "AUD", "CHF", "JPY", "INR"), "cash"),
    **dict.fromkeys(("USDC", "USDT", "ETH", "BTC", "SOL"), "crypto"),
    **dict.fromkeys(("XTR", "POINTS"), "points"),
    "CREDITS": "site-balance",
}

SYMBOL_CURRENCIES = {"$": "USD", "€": "EUR", "£": "GBP"}

_AMOUNT = r"(?:[0-9]{1,3}(?:,[0-9]{3})+|[0-9]+)(?:\.[0-9]+)?"
_CURRENCY = r"USD|EUR|GBP|CAD|AUD|CHF|JPY|INR|USDC|USDT|ETH|BTC|SOL|XTR|POINTS|CREDITS"
_CORE = re.compile(
    rf"(?:"
    rf"(?P<symbol>[$€£])?\s*(?P<amount>{_AMOUNT})\s*(?P<after>{_CURRENCY})?"
    rf"|(?P<before>{_CURRENCY})\s*(?P<before_symbol>[$€£])?\s*(?P<other_amount>{_AMOUNT})"
    rf")",
    re.IGNORECASE,
)


def _parse_core(text):
    """Return the amount and currency when the entire core is valid."""
    match = _CORE.fullmatch(text)
    if match is None:
        return None

    symbol = match.group("symbol") or match.group("before_symbol")
    currency = match.group("after") or match.group("before")
    currency = currency.upper() if currency else None
    if currency is not None and currency not in CURRENCY_KINDS:
        return None
    if symbol:
        default_currency = SYMBOL_CURRENCIES[symbol]
        allowed = {default_currency}
        if symbol == "$":
            allowed.update({"USDC", "USDT"})
        if currency is not None and currency not in allowed:
            return None
        currency = currency or default_currency
    if currency is None:
        return None

    amount = match.group("amount") or match.group("other_amount")
    return Decimal(amount.replace(",", "")), currency


def parse_reward(text):
    """Parse one supported reward, returning unknown for ambiguous inputs."""
    unknown = {"amount": None, "currency": None, "kind": "unknown"}
    text = text.strip()

    # Remove the optional decorations in the order defined by the grammar.
    text = re.sub(r"^(?:reward|bounty)\s*:\s*", "", text, flags=re.IGNORECASE)
    text = re.sub(r"^(?:(?:up\s+to|approximately)\s+|~\s*)", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\s*\(test\s+fixture\)$", "", text, flags=re.IGNORECASE)

    balance = re.search(
        r"(?:\s+(?:gross\s+of\s+)?site\s+balance|\s*\(site\s+balance\))$",
        text,
        flags=re.IGNORECASE,
    )
    if balance:
        text = text[: balance.start()]

    parsed = _parse_core(text.strip())
    if parsed is None:
        return unknown
    amount, currency = parsed
    return {
        "amount": amount,
        "currency": currency,
        "kind": "site-balance" if balance else CURRENCY_KINDS[currency],
    }
