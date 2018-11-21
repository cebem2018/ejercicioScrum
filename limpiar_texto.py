
def limpiar(texto: str) -> str:
    texto = texto.strip()
    return " ".join(texto.split())

if __name__ == "__main__":
    texto = "estoy escribiendo desde  móvil y meto un espacio al   final y algunos   por enmedio "
    texto_limpio = limpiar(texto)
    print("Texto original: '{}'".format(texto))
    print("Texto limpiado: '{}'".format(texto_limpio))
