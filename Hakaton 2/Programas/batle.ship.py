import numpy as np
def abrir(x):
    archive=open(x,"r",encoding="utf-8")
    return archive

archivo=abrir("battle.txt")
linea=archivo.readline().strip()

mapa1=np.zeros([8,8])
mapa2=np.zeros([8,8])
l=0
filas=[1,2,3,4,5,6,7,8]
columnas=["A","B","C","D","E","F","G","H"]
c=0
f=0
jugadas=[]

while linea!="":
    if l<8:
        partes=linea.split("-")
        lista1=[]
        for i in range(len(partes)):
            lista1.append(partes[i])
            
        for j in range(len(lista1)):
            mapa1[c][j]=lista1[j]
        c+=1
    if l>=8 and l<=15:
        hola=linea.split("-")
        lista2=[]
        for i in range(len(hola)):
            lista2.append(hola[i])
            
        for k in range(len(lista2)):
            mapa2[f][k]=lista2[k]
        f+=1
        
    if l>15:
        poto=linea.split(",")
        jugadas.append(poto[0])
        jugadas.append(poto[1])
        
    l+=1
    linea=archivo.readline().strip()
    
    
for i in range(len(jugadas)):
    if i%2==0:
        partes=jugadas[i].split(" ")
        letra=(partes[0][0])
        numero=int(partes[0][1])
        if mapa2[filas.index(numero)][columnas.index(letra)]==1:
            mapa2[filas.index(numero)][columnas.index(letra)]=0
        
    if i%2!=0:
        partes=jugadas[i].split(" ")
        letra=(partes[0][0])
        numero=int(partes[0][1])
        if mapa1[filas.index(numero)][columnas.index(letra)]==1:
            mapa1[filas.index(numero)][columnas.index(letra)]=0
    



mapa1_conta=0
mapa2_conta=0
for fil in range(len(filas)):
    for col in range(len(columnas)):
        mapa1_conta+=mapa1[fil][col]
        mapa2_conta+=mapa2[fil][col]

if mapa1_conta>mapa2_conta:
    print("gana jugador 1")
if mapa1_conta==mapa2_conta:
    print("empate")
if mapa1_conta<mapa2_conta:
    print("gana jugador 2")


        
        
     
    
        
        
                
            

    
    
    
