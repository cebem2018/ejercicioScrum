#Vamos a escribir cada elemento de una lista en una linea
# Lista con las lineas a escribir en el fichero
lineas = ['Uno', 'Dos', 'Tres', 'Cuatro', 'Cinco', 'Seis', '...']

dirFichero = './fichero_escribir.txt'
#opción 'w' (si existe el fichero borra su contenido y si no existe lo crea)
#opción 'a+' que se posiciona al final del fichero sin borrar su contenido y
#  en este caso empieza a escribir contenido a partir de esa posición.
fichero = open(dirFichero, 'w')
for l in lineas:
    #con el metodo write() escribimos el contenido que le pasamos como param.
    fichero.write(l + '\n')
fichero.close()

#hacemos test con el siguiente codigo
#python -m doctest -v nombre.py