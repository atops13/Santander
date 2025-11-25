# Ejercicio autocompletar
# crea una lista con los cuadrados de los n primeros numeros naturales
def cuadrados(n):
    lista = []
    for i in range(1, n+1):
        lista.append(i**2)
        
    return lista

print(cuadrados(10))

    

def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Ejemplo de uso:
print(es_primo(7))   # True
print(es_primo(10))  # False
# Versión optimizada de la función es_primo utilizando algunas mejoras:

def es_primo_optimizada(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Ejemplo de uso:
print(es_primo_optimizada(7))   # True
print(es_primo_optimizada(10))  # False
print(es_primo_optimizada(97))  # True

