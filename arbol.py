def xmas(n):
    # Espacios en blanco
    z = n - 1

    # "+" a colocar
    x = 1

    for i in range(n):
        print(' ' * z + '+' * x + ' ' * z)
    
        # Añadimos 1 "+" a los lados del anterior y reducimos un espacio en blanco
        x+=2
        z-=1
xmas(5)