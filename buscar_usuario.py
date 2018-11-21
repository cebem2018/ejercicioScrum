list=['jose','carlos','juan']

def buscaUsuario(lista, usuario):
  """
  Este metodo sirve para buscar un usuario en una lista
  >>> buscaUsuario(['jose','carlos','juan'],'jose')
  True
  """

  if usuario in list:
      print 'ese usuario existe'
      return True
  else:
      print 'ese usuario no existe'
      return False


if __name__ == "__main__":
  import doctest
  doctest.testmod()

documentacion = buscaUsuario.__doc__
print("El comentario de documentacion:",documentacion)

print("El nombre del metodo es:",buscaUsuario.__name__)