import numpy as hola



            
            
archive=open("battle.txt","r",encoding="utf-8")
linea=archive.readline().strip()

columnas=["A","B","C","D","E","F","G","H"]
fila=["1","2","3","4","5","6","7","8"]
mapa1=hola.zeros([20,8])
mapa2=hola.zeros([20,9])

c=0
f=0
i=0
while linea!="":
    i+=1                     
    partes=linea.split("-")    
    if i<=8:
        lista1=[]
        for j in range(8):
            lista1.append(int(partes[j]))
        for p in range(len(lista1)):
            mapa1[c][p]=lista1[p]
        c+=1
    if i>8 and i<17:
        lista2=[]
        for ñ in range(8):
            lista2.append(int(partes[ñ]))
        for o in range(len(lista2)):
            mapa2[f][o]=lista2[o]
        f+=1
        
    if i>=17:
        parte=linea.split(",")
       # letra1=parte[0][0]
        #numero1=parte[0][1]
        jugador1.append(parte[0])
        jugador2.append(parte[1])
        #print(letra1,numero1)
    linea=archive.readline().strip()


        
    
         

        
        
    
                
            
            
     
     
        
    
        
            
    

        

