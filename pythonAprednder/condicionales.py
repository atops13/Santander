# if, elfi, else

import os
os.system("cls")  # Limpiar pantalla

edad = 15

if edad >= 18:
    print("Eres mayor de edad", edad)
else:
    print("Eres menor de edad", edad)
     
nota = 2

if nota >= 9:
    print("Sobresaliente")
elif nota >= 7:
    print("Notable")
elif nota >= 6:
    print("Bien")
elif nota >= 5:
    print("Suficiente")
else:
    print("Insuficiente")
# Una vez entrada una condicion verdadera, el resto se ignora

# Condicionales multiples

edad= 15
tiene_carnet = False

if edad >= 18 and tiene_carnet:
    print("Puedes conducir")
else:
    print("No puedes conducir!!")

if edad >= 18 or tiene_carnet:
    print("Puedes conducir")
else:
    print("paga melon")

if not tiene_carnet:
    print("No conduces")

mensaje = "Eres mayor de edad" if edad >= 18 else "Eres menor de edad"
print(mensaje)