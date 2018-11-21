def dime_forma():
  """Metodo que muestra al usuario el menu de seleccion de figuras"""
  print("Dime cual es la forma que quieres calcular")
  print("      1- Cuadrado")
  print("      2- Restangulo")
  print("      3- Circunferencia")
  print("      4- Triangulo")
  print("      5- Salir")
  return int(input("¿que quieres hacer? "))

def calcula_cuadrado(lado):
  """Metodo que calcula el area de un cuadrado"""
  """
  >>>calcula_cuadrado(5)
  25
  """
  return lado*lado

def calcula_rectangulo(base,altura):
  """Metodo que calcula el area de un rectangulo"""
  """
  >>>calcula_rectangulo(5,2)
  10
  """
  return base*altura

def calcula_circunferencia(radio):
  """Metodo que calcula el area de una circunferencia"""
  """
  >>>calcula_circunferencia(1)
  2*math.pi
  """
  return (2+radio*math.pi)

def calcula_triangulo(base,altura):
  """Metodo que calcula el area de un triangulo"""
  """
  >>>clacula_triangulo(1,2)
  1
  """
  return (base*altura)/2


forma=dime_forma()
while(forma!=5):
  if(forma==1):
    lado=int(input("Dime el lado del cuadrado: "))
    print("La superficie del cuadrado es: ",calcula_cuadrado(lado))
  elif(forma==2):
    base=int(input("Dime el lado del rectangulo: "))
    altura=int(input("Dime la altura del rectangulo: "))
    print("La superficie del restangulo es: ",calcula_rectangulo(base,altura))
  elif(forma==3):
    radio=int(input("Dime el radio de la circunferencia: "))
    print("La superficie de la circunferencia es: ",calcula_circunferencia(radio))
  elif(forma==4):
    base=int(input("Dime el lado del rectangulo: "))
    altura=int(input("Dime la altura del rectangulo: "))
    print("La superficie del restangulo es: ",calcula_triangulo(base,altura))  
  else:
    print("Opcion no reconocida")
  forma=dime_forma()
print("--Programa Terminado--")

if __name__ == "__main__":
  import doctest
  doctest.testmod()