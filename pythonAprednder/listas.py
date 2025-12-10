#listas, secuencias mutables de elementos

print("\n Mi primera lista")
lista1 = [1, 2, 3, 4, 5]
lista2 = ["Hola", "que", "tal"]
lista3 =[1, "Hola", 3.14, True]

lista_grande = [lista1, lista2, lista3]

matriz = [[1, 2], [3, 4]]

print(lista1)
print(lista2)   
print(lista3)
print(lista_grande)
print(matriz)

print("\n Acceder a elementos de la lista")
print(lista2[0])  # primer elemento
print(lista1[-1])  # ultimo elemento, cuenta desde el final
print(lista_grande[1][0])  # accediendo a un elemento de una sublista

#slicing de listas
print("\n Slicing de listas")
print(lista1[1:4])  # elementos desde el indice 1 al 3
print(lista2[:2])   # primeros dos elementos
print(lista3[2:])   # desde el indice 2 hasta el final

#modificar listas

lista1[0] = 10
lista1 += [6, 7, 8]  # concatenar listas
lista2.append("amigo")  # agregar un elemento al final
print("\n Listas modificadas", lista1, lista2)
