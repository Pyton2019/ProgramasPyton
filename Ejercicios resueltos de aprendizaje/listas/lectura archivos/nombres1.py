lista=[] #se guardaran los nombres ke estan en el archivo 1
lista1=[] # se guardaran los nombres de la lista 2
arch=open("nombres.txt","r")
linea=arch.readline().strip()
while linea!="":
    Nombresss=linea    # como solo tiene una palabra en la fila no se pone el comando linea.split(",")
    lista.append(Nombresss)
    
    linea=arch.readline().strip()

arch1=open("nombre1.txt","r")
linea=arch1.readline().strip()
while linea!="":
    Nombress2=linea
    lista1.append(Nombress2)
    
    
    linea=arch1.readline().strip()
    
   
x=set(lista)    #te dice todos los integrantes de la lista eliminando los repetidos 
f=set(lista) &set(lista1)    # te dice los integrantes ke salen en las dos listas    
print(x)
print(f)

    
    

    
    
