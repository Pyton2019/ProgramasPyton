
def total_lista(f):  # funcion para saber el total de elementos en la lista
    return(f)
    
lista=[] # se guardaran los numeros del archivo

arch=open("ejercicio1.txt", "r")
linea=arch.readline().strip()
while linea!="":
    numerossss=int(linea)
    lista.append(numerossss)
    
    linea=arch.readline().strip()


x=total_lista(len(lista))   #total elementos de la lista

d=0 # sumador numeros de la lista
for i in lista:
    d=d+i
    
promedio= d/x

limite=int(promedio*0.9)   #ya ke se necesita buscar los numeros ke estan entre los limites del 10% del promedio de cada lado
limite1=int(promedio*1.1)

c=0  #contador numeros entres los promedios +-10%
print("Limite 1",":",limite)
for i in range(limite,limite1+1): #como ya lo incluye el 10% en el limite por lo tanto keda asi   
    print(i)
    c=c+1
print("Limite2 :",limite1)    
print("Hay",c,"numeros entre +-10% del promedio de todo estos")

    
    
            

    
    
    


    
    
    
    
    