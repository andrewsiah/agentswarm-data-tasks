def drop_suffix(text: str, token: str) -> str:
    """
    Removes one matching edge token from the end of the text.
    """
    if type(text) is not str or type(token) is not str:
        raise TypeError("Text and token must be strings.")
    if len(text) > 1000:
        raise ValueError("Text exceeds maximum length.")
    if len(token) > 64:
        raise ValueError("Token exceeds maximum length.")
    return text.removesuffix(token) 
