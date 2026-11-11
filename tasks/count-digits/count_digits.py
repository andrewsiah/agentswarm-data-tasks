def count_digits(texto: str) -> int:
    """
    Cuenta los dígitos ASCII del '0' al '9' en una cadena de texto,
    ignorando todos los demás caracteres y los dígitos no ASCII.
    """
    if type(texto) is not str:
        raise TypeError("El argumento debe ser estrictamente de tipo str nativo.")
    
    if len(texto) > 1000:
        raise ValueError("La cadena excede el límite máximo permitido de 1000 caracteres.")
    
    conteo = 0
    for char in texto:
        if '0' <= char <= '9':
            conteo += 1
            
    return conteo