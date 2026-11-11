def is_palindrome(text):
    if type(text) is not str:
        raise TypeError("text must be an exact built-in str")
    if len(text) > 1000:
        raise ValueError("text must be at most 1000 Unicode code points")
    kept = [
        ch.lower()
        for ch in text
        if ("a" <= ch <= "z") or ("A" <= ch <= "Z") or ("0" <= ch <= "9")
    ]
    return kept == kept[::-1]
