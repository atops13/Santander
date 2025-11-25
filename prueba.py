print("hola mundo")
  
for i in range(5):
    print("hola")

# calcular el factorial de un numero dado
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

def suma_lista(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + suma_lista(lista[1:])

print(suma_lista([1,2,3,4,5]))
