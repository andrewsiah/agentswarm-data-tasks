def pad_left(text, width, fill):
    """Left-pad ``text`` to ``width`` code points using ``fill``."""
    if type(text) is not str:
        raise TypeError("text must be str")
    if type(width) is not int:
        raise TypeError("width must be int")
    if type(fill) is not str:
        raise TypeError("fill must be str")

    if len(text) > 64:
        raise ValueError("text is too long")
    if width < 0 or width > 128:
        raise ValueError("width is out of range")
    if len(fill) != 1:
        raise ValueError("fill must contain exactly one code point")

    padding = width - len(text)
    if padding <= 0:
        return text
    return fill * padding + text
