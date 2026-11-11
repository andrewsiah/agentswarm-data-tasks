def drop_prefix(text, token):
    if type(text) is not str:
        raise TypeError("text must be an exact built-in str")
    if type(token) is not str:
        raise TypeError("token must be an exact built-in str")
    if len(text) > 1000:
        raise ValueError("text must be at most 1000 code points")
    if len(token) > 64:
        raise ValueError("token must be at most 64 code points")
    if token and text.startswith(token):
        return text[len(token):]
    return text
