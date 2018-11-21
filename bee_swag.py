def texto_con_swag(string):
    """Invierte el texto recibido entre mayusculas/minusculas
    >>> texto_con_swag("hEY YO hOMIE")
    'Hey yo Homie'
    """
    return string.swapcase()
if __name__ == "__main__":
    string = "hEY YO hOMIE"
    print(texto_con_swag(string))