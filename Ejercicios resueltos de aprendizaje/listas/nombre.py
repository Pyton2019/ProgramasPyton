nombre1=[] #nombres no repetidos
nombre=[]
arch=open("nombres.txt","r")
linea=arch.readline().strip()

while linea!="":
    nombreslista=linea
    nombre.append(nombreslista)
    x=nombre.count(nombreslista)
    if x==1:
        nombre1.append(nombreslista)
    if x==2:
        nombre1.remove(nombreslista)  # remueve el nombre que cuenta como 2 veces con el comando count de arriba
    
    linea=arch.readline().strip()
    
print(nombre1)


    
lista=[1,1,2,3,4,2,4,3]



x=min(lista)
y=max(lista)
print(x)
print(y)
