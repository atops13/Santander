# Bloques de codigo reutilizables

"""     Definicion de funciones

def nombre_funcion(parametro1, parametro2,....):
    # docstring
    # bloque de codigo
    return valor_a_devolver
"""
def saludar( ):
    """Funcion que saluda a la persona cuyo nombre se pasa como parametro"""
    print("hola")


# llamada a la funcion

saludar()

def saludar(nombre):
    """Funcion que saluda a la persona cuyo nombre se pasa como parametro"""
    print(f"hola {nombre}")

saludar("Antonio")

# nombre es parametro, antonio es argumento

def sumar (a,b):
    suma = a +b
    return suma

resultado = sumar (3,5)
print(f"La suma es: {resultado}")

# documentacion de funciones
def restar (a,b):
    """Funcion que resta dos numeros y devuelve el resultado"""
    return a - b

print(restar.__doc__)  # muestra la documentacion de la funcion

# parametros por defecto

print("\n Parametro por defecto")
def multiplicar (a, b=2):
     """Funcion que multiplica dos numeros, el segundo es por defecto 2"""
     return a * b
print(multiplicar(4))  # usa el valor por defecto de b
print(multiplicar(4,5))  # usa el valor proporcionado para b

# Argumentos por clave

def describir_persona(nombre, edad, sexo):
    print(f"Nombre: {nombre}, Edad: {edad}, Sexo: {sexo}")

describir_persona("anto","43","gato") #parametros por posicion
describir_persona(edad="43", nombre="anto", sexo="gato") #parametros por clave

# parametros longitud variables

print("\n Parametros longitud variable")

def sumar_numeros(*numeros):
    """Funcion que suma una cantidad variable de numeros"""
    return sum(numeros)

print(sumar_numeros(1,2,3,4,5))

def restar_numeros(*numeros):
    """Funcion que resta una cantidad variable de numeros"""
    resta = 0
    for num in numeros:
        resta -= num
    return resta

print(restar_numeros(1,2,3,4,5))

# Argumentos de clave-valor

def mostrar_info(**kwargs):
    """Funcion que muestra la informacion de una persona"""
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Antonio", edad=43, ciudad="Madrid")
mostrar_info(pais="España", profesion="Desarrollador")
mostrar_info()  # llamada sin argumentos

