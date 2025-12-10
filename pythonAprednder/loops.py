#bucles while y break
import os
os.system("cls")

i = 0
while i < 5:
    print(i)
    i += 1

#while True:
#    print(i)
#   i += 1
#    if i == 10:
#        break # util cuando necesitas una condicion y no sabes las iteraciones

print("Bucle con continue")

i = 0

while i < 10:
    i += 1

    if i % 2 == 0:
        continue  # saltar el resto del codigo y volver al inicio del bucle
    print(i)


# se puede usar else con while, para poner un mesnsaje al terminar el bucle
# si se termina con break ese mensaje no sale asi que es util aveces

# Bucle for
frutas = ["manzana", "banana", "cereza","mango","pera"]

for fruta in frutas:
    print(fruta)

# recuperar indice

for indice, fruta in enumerate(frutas):
    print(indice, fruta)

# bucles anidados
letras = ["a", "b", "c"]
numeros = [1, 2, 3]

for letra in letras:
    for numero in numeros:
        print(f"{letra} x {numero}")


# list comprehension

print("\n List Comprehension")

animales = ["perro", "gato", "conejo", "tortuga"]
animales_mayusculas = [animal.upper() for animal in animales]

print(animales_mayusculas)

# mostrar pares de una lista

pares =[num for num in [1,2,3,4,5,6,7,8,9,10] if num % 2 == 0]
print(pares)