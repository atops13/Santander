# forma para pedirle al usuario que ingrese informacion

print("¿Cual es tu nombre?")
nombre = input()
print(f"Hola {nombre}, bienvenido!")
edad= input("¿Cual es tu edad?")
print(f"Tienes {edad} años, vaya vaya que graade estas hecho {nombre}!")

#todo el input se toma como string

print("Dime donde vives, pais y ciudad:")
pais ,ciudad = input("Donde vives? \n").split( ) #separar por espacios,
#se puede separar por cualquier cosa con split("separador")
print(f"Vives en {ciudad} que esta en {pais}")


