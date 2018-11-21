import random


numRandom=random.randrange(10)

print("Adivina un número del 0 al 10")

a=input()

while(int(a)!=numRandom):
    print("Has fallado, introduce otro numero")
    a=input()

print("Has acertado!")

print(numRandom)