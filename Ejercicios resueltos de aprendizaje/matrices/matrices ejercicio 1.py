import numpy as np

def buscar_agregar(lista,elemento):
    if not elemento in lista:
        lista.append(elemento)
    return lista.index(elemento)            #paque retorne el numero de la posicion 



def mayor(matriz):            #funcion para sumar las columnas hacia abajo
    mayor1=-999999999
    for c in range(10):       
        suma=0
        for f in range(10):
            suma=suma+matriz[f][c]
        if suma>mayor1:
            mayor1=suma
            nombre1=paises[c]
    print("La ciudad mas visitada fue",nombre1,"con",mayor1,"veces")
            
paises=[]
nombres=[]
matriz=np.zeros([10,10])

arch=open("nombre.txt","r")
linea=arch.readline().strip()
while linea!="":
    partes=linea.split(",")
    nombre=partes[0]
    pais=partes[1]
    año=int(partes[2])
    
    columna=buscar_agregar(paises,pais)
    fila=buscar_agregar(nombres,nombre)
    
    matriz[fila][columna]=(matriz[fila][columna])+1    #la hago como contador la variable debido a que cada vez que la persona visita el pais le agrega uno al anterior numero que habia
    
    linea=arch.readline().strip()


for fil in range(len(nombres)):
    for col in range(len(paises)):
        if matriz[fil][col]!=0:
            print(nombres[fil],"visito",matriz[fil][col],"veces",paises[col])
            

x=mayor(matriz)
     
    
    

    

