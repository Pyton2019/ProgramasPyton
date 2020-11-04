import numpy as np

matriz=np.zeros([20,12])

archive=open("ventas.txt","r",encoding="utf-8")
linea=archive.readline().strip()
ciudad1=[]
año=["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
conta_registro_totales=0
conta_registro=0
while linea!="":
    partes=linea.split(",")
    ciudad=partes[0]
    ventas=int(partes[1])
    horas=partes[2]
    mes=partes[3]
    
    hora1=horas.split(":")
    for i in range(len(hora1)):
        if i==0:
            hora=hora1[i]
        else:
            minutos=hora1[i]
    
    if int(hora)>=8 and int(hora)<18:
       
        if ciudad not in ciudad1:
            ciudad1.append(ciudad)
        
        y=año.index(mes)
        x=ciudad1.index(ciudad)
       
       
        matriz[x][y]+=(ventas)
    else:
         conta_registro+=1
    conta_registro_totales+=1
    linea=archive.readline().strip()
    
total_ventas=0  
for col in range(len(año)):
    suma=0
    for fil in range(len(ciudad1)):
        
        suma+=matriz[fil][col]
    total_ventas+=suma
        
    print(año[col],suma)
    
for fil in range(len(ciudad1)):
    suma1=0
    for col in range(len(año)):
        suma1+=matriz[fil][col]
    
    print(ciudad1[fil],round(suma1/len(año),2))
        
    
print(conta_registro*100/conta_registro_totales,"%")
        
        
    