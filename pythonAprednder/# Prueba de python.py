# Prueba de python
print("Hola,mundos")

print("hola","mariconas",sep="---")

# Tipo de datos
entero=10
print(entero,type(entero))

print(845432+1,type(845432+1))

print(10e4,type(10e4))

print(1>2,type(1>2))

print(None,type(None))

#casting

texto="100"
print(int(texto) + 2)
print(texto + "2")

print(int(2.5)) #elimina la parte decimal

print(round(2.5)) #redondea al entero PAR mas cercano

#tipo de variables

nombre = "Antonio"
edad = 28
estatura = 1.92
mayor_de_edad = True
print("Nombre:",nombre)
print("Edad:",edad) 
print("Estatura:",estatura)
print("¿Es mayor de edad?",mayor_de_edad)
#no existe el concepto de constantes en python,
#  con masyuscula se suele indicar que una variable no debe cambiar 

#tipado dinamico

#nombre=123
#print(type(nombre)) #cambia de str a int sin hacer mucho mas que ponerlo

print(f"Hola mi nombre es {nombre} y tengo {edad} años.")

#types anotation
nombre: str = "Antonio"
esta_conecatado: bool = True
 #solo sirve para documentacion y ayuda a editores de codigo
 #se puede poner en estrict mode para que de error si no se cumple


