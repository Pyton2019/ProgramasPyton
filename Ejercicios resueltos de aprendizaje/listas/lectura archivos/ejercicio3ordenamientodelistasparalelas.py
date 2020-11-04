

arch=open("ejercicio3.txt","r")
linea=arch.readline().strip()

nombres=[]
puntajes=[]
penalizaciones=[]
while linea!="":
    partes=linea.split(",")
    nombre=partes[0]
    tiempo1=float(partes[1])
    tiempo2=float(partes[2])
    tiempo3=float(partes[3])
    penali1=float(partes[4])
    penali2=float(partes[5])
    penali3=float(partes[6])
    
    promedio=(tiempo1+tiempo2+tiempo3)/3  #promedio de los tres tiempos de cada jugador
    penali=penali1+penali2+penali3  #suma de penalizaciones de cada jugador
    puntaje=promedio+penali   # puntaje de cada jugador
    
    
    
    nombres.append(nombre)
    puntajes.append(puntaje)
    penalizaciones.append(penali)
    
    
    linea=arch.readline().strip()
    

for a in range(len(nombre)-1):
    for b in range(a+1,len(nombre)):
        if puntajes[a]>puntajes[b]:
            aux=puntajes[a]
            puntajes[a]=puntajes[b]
            puntajes[b]=aux
            
            aux2=nombres[a]
            nombres[a]=nombres[b]
            nombres[b]=aux2
            
            aux3=penalizaciones[a]
            penalizaciones[a]=penalizaciones[b]
            penalizaciones[b]=aux3
            
for i in range(3):
    
    print(f"El lugar{i+1} fue para {nombres[i]} con un tiempo de {puntajes[i]} ({penalizaciones[i]})")
            
    

