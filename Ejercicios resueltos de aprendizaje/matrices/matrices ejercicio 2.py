import numpy as np

arch=open("ciudades.txt","r")
linea=arch.readline().strip()


def buscar_agregar(lista,elemento):
    if not elemento in lista:
        lista.append(elemento)
    return lista.index(elemento)

def buscar(lista,elemento):
    valor=-1
    if  elemento in lista:    # yaque hay qque comparar si la ciudad esta en la lista 
        valor=lista.append(elemento)
    else:
        valor=0
    return valor



matriz=np.zeros([13,15])
ciudades=[]       # guardo primeras ciudades

while linea!="":
    partes=linea.split(",")
    ciudad1=partes[0]
    ciudad2=partes[1]
    distancia=int(partes[2])
    
    
    ciudades.append(ciudad1)
    ciudades.append(ciudad2)
    
    columna=buscar_agregar(ciudades,ciudad1)      #posicion de la columna 
    print(columna)
    fila=buscar_agregar(ciudades,ciudad2)    #posicion de la fila
    
    matriz[fila][columna]=distancia  
    matriz[columna][fila]=distancia   
    linea=arch.readline().strip()
    
for fil in range(len(ciudades)):
    print(ciudades[fil])
    for col in range(len(ciudades)):
        print(ciudades[col],matriz[fil][col])
    
arch.close
"""
arch2=open("ciudades2.txt","r")
linea2=arch2.readline().strip()
while linea2!="":                        
    partes1=linea2.split(",")
    ciudad1=partes1[0]
    ciudad2=partes1[1]
    
    columna=buscar(ciudades,ciudad1)   # evaluao si las nuevas ciudades estan en la lista 
    fila=buscar(ciudades,ciudad2)
    
    if columna==-1:
        print(ciudad1,"no existe")
        
    elif fila==-1:
        print(ciudad2,"no existe") 
        
    elif (matriz[fila][columna])==0:
        print(ciudad1,"-",ciudad2,"no estan conectadas")
        
        
    else:
        print(ciudad1,"-",ciudad2,"estan a",(matriz[fila][columna]),"de distancia")
        
    linea2=arch2.readline().strip()
arch2.close
    
"""
    
    