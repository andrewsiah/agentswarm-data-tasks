"""Parse one reward string; see SPEC.md."""
from decimal import Decimal
import re

def parse_reward(text: str) -> dict:
    """Parse one reward string; see SPEC.md."""
    if not isinstance(text, str):
        return {"amount": None, "currency": None, "kind": "unknown"}
    
    s = text.strip()
    if not s:
        return {"amount": None, "currency": None, "kind": "unknown"}
    
    # Optional prefix: reward: or bounty:
    prefix_pattern = re.compile(r"^(?:reward|bounty)\s*:\s*", re.IGNORECASE)
    s = prefix_pattern.sub("", s).strip()
    
    # Optional trailing test fixture suffix: (test fixture)
    test_fixture_pattern = re.compile(r"\s*\(\s*test\s+fixture\s*\)\s*$", re.IGNORECASE)
    s = test_fixture_pattern.sub("", s).strip()
    
    # Optional site balance suffix override
    # Suffixes: 'site balance', '(site balance)', 'gross of site balance'
    balance_suffix_pattern = re.compile(
        r"\s+(?:gross\s+of\s+site\s+balance|site\s+balance|\(\s*site\s+balance\s*\))\s*$",
        re.IGNORECASE
    )
    has_site_balance_suffix = bool(balance_suffix_pattern.search(s))
    s = balance_suffix_pattern.sub("", s).strip()
    
    # Optional qualifiers: up to, approximately, ~
    qualifier_pattern = re.compile(r"^(?:up\s+to|approximately|~)\s+", re.IGNORECASE)
    s = qualifier_pattern.sub("", s).strip()
    
    # Now s should contain amount and currency in either order, optionally with symbol
    # Symbols: $, €, £
    # Currencies:
    # Cash: USD, EUR, GBP, CAD, AUD, CHF, JPY, INR
    # Crypto: USDC, USDT, ETH, BTC, SOL
    # Points: XTR, points
    # Site-balance: credits (or CREDITS)
    
    cash_currencies = {"USD", "EUR", "GBP", "CAD", "AUD", "CHF", "JPY", "INR"}
    crypto_currencies = {"USDC", "USDT", "ETH", "BTC", "SOL"}
    points_currencies = {"XTR", "POINTS"}
    site_currencies = {"CREDITS"}
    
    symbol_to_cash = {
        "$": "USD",
        "€": "EUR",
        "£": "GBP"
    }
    
    # We can tokenize or regex match amount and currency.
    # An amount is ASCII digits, optionally properly grouped by commas in groups of three, optionally followed by a dot and one or more digits.
    # No sign, exponent, decimal comma, range or multiple amounts.
    # Regex for amount: (?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?
    amount_regex = r"(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?"
    
    # Pattern allowing symbol attached or separate, currency token, amount
    # Let's match tokens in the string. There should be exactly one amount and one currency token (plus optional symbol).
    # Clean up multiple whitespaces
    parts = re.split(r"\s+", s)
    if len(parts) > 3 or len(parts) < 1:
        return {"amount": None, "currency": None, "kind": "unknown"}
    
    raw_amount = None
    raw_currency_token = None
    raw_symbol = None
    
    # Let's inspect parts or use a flexible regex that extracts amount, symbol, currency token.
    # A comprehensive regex approach:
    # Symbol can be at start of amount or standalone or attached to currency/amount.
    # Let's match using regex on the whole string s:
    # Format 1: [symbol]amount currency OR currency [symbol]amount OR [symbol] amount currency etc.
    
    # Let's parse tokens more precisely.
    tokens = []
    for p_item in parts:
        # Check if item contains symbol
        for sym in ["$", "€", "£"]:
            if sym in p_item:
                # split symbol if attached
                if p_item.startswith(sym):
                    if raw_symbol is not None and raw_symbol != sym:
                        return {"amount": None, "currency": None, "kind": "unknown"}
                    raw_symbol = sym
                    p_item = p_item[len(sym):]
                elif p_item.endswith(sym):
                    if raw_symbol is not None and raw_symbol != sym:
                        return {"amount": None, "currency": None, "kind": "unknown"}
                    raw_symbol = sym
                    p_item = p_item[:-len(sym)]
        if p_item:
            tokens.append(p_item)
            
    if len(tokens) > 2:
        return {"amount": None, "currency": None, "kind": "unknown"}
        
    amount_str = None
    curr_str = None
    
    for t in tokens:
        if re.fullmatch(amount_regex, t):
            if amount_str is not None:
                return {"amount": None, "currency": None, "kind": "unknown"}
            amount_str = t
        else:
            if curr_str is not None:
                return {"amount": None, "currency": None, "kind": "unknown"}
            curr_str = t
            
    if not amount_str:
        return {"amount": None, "currency": None, "kind": "unknown"}
        
    # Parse amount with Decimal
    try:
        clean_amt_str = amount_str.replace(",", "")
        amount_dec = Decimal(clean_amt_str)
        if amount_dec.is_nan() or amount_dec.is_infinite() or amount_dec < 0:
            return {"amount": None, "currency": None, "kind": "unknown"}
    except Exception:
        return {"amount": None, "currency": None, "kind": "unknown"}
        
    # Determine currency and kind
    currency = None
    kind = None
    
    if curr_str is not None:
        upper_curr = curr_str.upper()
        if upper_curr in cash_currencies:
            currency = upper_curr
            kind = "cash"
        elif upper_curr in crypto_currencies:
            currency = upper_curr
            kind = "crypto"
        elif upper_curr in points_currencies:
            currency = upper_curr
            kind = "points"
        elif upper_curr in site_currencies:
            currency = upper_curr
            kind = "site-balance"
        elif upper_curr == "POINTS":
            currency = "POINTS"
            kind = "points"
        elif upper_curr == "CREDITS":
            currency = "CREDITS"
            kind = "site-balance"
        else:
            return {"amount": None, "currency": None, "kind": "unknown"}
            
    # Handle symbol and currency conflict checks
    if raw_symbol is not None:
        symbol_currency = symbol_to_cash[raw_symbol]
        if currency is None:
            currency = symbol_currency
            kind = "cash"
        else:
            # Symbol plus matching cash code is allowed
            # $ plus USDC/USDT is also allowed
            # Other symbol/code conflicts are unknown
            if currency == symbol_currency:
                pass
            elif raw_symbol == "$" and currency in {"USDC", "USDT"}:
                pass
            else:
                return {"amount": None, "currency": None, "kind": "unknown"}
                
    if currency is None:
        return {"amount": None, "currency": None, "kind": "unknown"}
        
    if has_site_balance_suffix:
        kind = "site-balance"
        
    return {
        "amount": amount_dec,
        "currency": currency,
        "kind": kind
    }

