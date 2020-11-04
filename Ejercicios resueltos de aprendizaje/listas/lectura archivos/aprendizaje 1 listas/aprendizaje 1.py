lista=[1,3,4]

lista[2]=7  # Para modificar un elemento de la lista

print(lista)

lista.append(lista[2]) # para agregar al final de la lista el elemento de la posicion 2

print(lista)

lista.remove(7)  #para remover un elemento y si esta repetido solo elimina uno 
print(lista)

lista.pop(0)      # elimina el elemento de la posicion 0
lista.pop()         # si no tiene ningun argumento eliminara el ke esta en la ultima posicion

print(lista)

del lista[0]   # lo mismo ke pop son para eliminar elemntos ke estan en esa posicion

print(lista)
