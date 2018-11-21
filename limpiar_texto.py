
def limpiar(texto: str) -> str:
<<<<<<< HEAD
    """El texto que recibe se devuelve limpio, eliminando espacios dobles y los espacios que haya
    tanto al principio como al final.
    :param texto: Texto de entrada
    :type texto: str
    :return: Texto de entrada limpio (eliminando 
    :rtype: str
    >>> limpiar("estoy escribiendo desde  móvil y meto un espacio al   final y algunos   por enmedio ")
    'estoy escribiendo desde móvil y meto un espacio al final y algunos por enmedio'
    """
=======
>>>>>>> 6211d31095bd5409d4ef3a031bf996043f540167
    texto = texto.strip()
    return " ".join(texto.split())

if __name__ == "__main__":
    texto = "estoy escribiendo desde  móvil y meto un espacio al   final y algunos   por enmedio "
    texto_limpio = limpiar(texto)
    print("Texto original: '{}'".format(texto))
    print("Texto limpiado: '{}'".format(texto_limpio))
