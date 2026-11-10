def drop_suffix(text: str, token: str) -> str:
    """
    Removes one matching edge token from the end of the text.
    """
    if type(text) is not str or type(token) is not str:
        raise TypeError("Text and token must be strings.")
    return text.removesuffix(token) 
