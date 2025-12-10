# Estructura muy imporante
import os

persona = {
    "nombre": "Antonio",
    "edad": 21,
    "ciudad": "Granada",
    "estudiante": True,
    "lenguajes": ["Python", "JavaScript", "C++"],
    "redes": {
        "twitter": "@antonio",
        "linkedin": "antonio-linkedin"
    }

}

# Acceder a valores

print(persona["nombre"])
print(persona["lenguajes"][2])
print(persona["redes"]["twitter"])

# Modificar valores

persona["edad"] = 22
print(f"Edad modificada: {persona["edad"]}")

# Eliminar propiedad

del persona ["edad"]
#print(f"Diccionario despues de eliminar edad: {persona}")

# recuperar propiedad

persona.pop("estudiante")
#print(persona)

# Merge de diccionarios

a = { "name": "Antonio", "age": 21}
b = { "name": "felipe",  "city":"Madrid"}

a.update(b)
print(a)

# Comprobar propiedad
print("city" in a)  # True
print("estudiante" in a)   # False 

# Obtener todas las claves y valores
claves = persona.keys()
valores = persona.values()
items = persona.items()

print(claves)
print(valores)
print(items)

# Recorrer diccionario
for clave, valor in persona.items():
    print(f"{clave}: {valor}")


# Ejercicio con dicconarios
# os.system("cls")

""" Haya la suma de 2 numeros que den una suma concreta 
"""
numeros = [2, 7, 11, 15]
objetivo = 26

def encontrar_pareja (numeros, goal):
    seen = {} # diccionario para almacenar numeros vistos

    for index, value in enumerate(numeros):
        missing = goal - value
        if missing in seen:
            return (seen[missing], index), seen
        seen[value] = index # Guardamos el numero actual con su indice
    return None, seen

resultado, seen = encontrar_pareja(numeros, objetivo)
print(f"Indices de los numeros que suman {objetivo}: {resultado}") 

print(f"Seen contiene: {seen}")

# 4h39min
# https://youtu.be/TkN2i-_4N4g?si=_1YQ6XlPG-n-neat
