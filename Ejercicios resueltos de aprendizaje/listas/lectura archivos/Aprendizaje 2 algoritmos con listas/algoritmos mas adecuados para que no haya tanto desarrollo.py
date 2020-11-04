#def maximo(lista):    # para obtener maximo o minimo cambiando el valor de la variable de una lista con funciones.
#    maxx=-99999
#    for i in lista:
#        if i>maxx:
#            maxx=i
#    return maxx
#    
#
#
#
#milista=[20,40,54,54,6,12,1,3]
#f=maximo(milista)
#
#maximo1=-8888        # variables puestas para poder imprimirlo por pantalla abajo
#maximo2=-777777
#
#maximo1=maximo(milista)
#milista.remove(maximo1)
#
#maximo2=maximo(milista)
#
#print("Los dos maximos son : ",maximo1,maximo2)
#print("la lista queda asi con el primer max eliminado: ",milista)


#def existe(lista,valor):
#    if valor in lista:            # para buscar si el valor esta en la lista
#        return True
#    else:
#        return False
#       
#listaa=[2,4,5,7,78,78,99,776,66,6,64,5,4]
#
#print("El valor puesto existe:",existe(listaa,99)) # 64 lo pongo para averiguar si dicho valor esta dentro de la lista

#
#listaaa=[2,3,5,6,7,8,8,89,2]   # en vez de llamar a una funcion hago esto
#
#print(78 in listaaa)
#print(2 in listaaa)

#def hola(valor,listaa):                #para saber la posicion del valor que se puso
#   if valor in lista:
#       return lista.index(valor)
#   else:
#       return -1     # si no esta en la lista retornamos con un -1
#        
#lista=[2,5,67,45,89,28]
#
#print("El valor puesto esta en la lista esta en la posicion:",hola(45,lista))


listaa=[2,4,8,9,54,32,1,91,3]
print(listaa)

for a in range(len(listaa)-1):      #for para recorrer todas las posiciones  menos una posicion
    for b in range(a+1,len(listaa)):  # para ver recorrer de la posicion siguente hasta el total de la lista
        if listaa[a]>listaa[b]:
            aux=listaa[a]
            listaa[a]=listaa[b]
            listaa[b]=aux
            
print(listaa)
            
        


