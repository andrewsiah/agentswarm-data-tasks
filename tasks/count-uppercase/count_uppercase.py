import string

def count_uppercase(text) -> int:
    """Cuenta las letras mayúsculas ASCII (A-Z) en una cadena dada (máximo 1000 caracteres)."""
    if type(text) is not str:
        raise TypeError("text must be an exact str")
    if len(text) > 1000:
        raise ValueError("text exceeds maximum allowed length of 1000 code points")
    
    return sum(1 for c in text if c in string.ascii_uppercase)