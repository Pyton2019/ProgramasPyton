nombres1=[]   #nombres riesgos altos
riesgo1=[]
nombres2=[]   # nombres riesgo medios
riesgo2=[]
nombres3=[]   # nombres riesgos bajos
riesgo3=[]

arch=open("ejercicio4.txt","r")
linea=arch.readline().strip()
while linea!="":
    partes=linea.split(";")
    nombre=partes[0]
    edad=int(partes[1])
    riesgos=float(partes[2])
    
    if edad>75:
        nombres1.append(nombre)
        riesgo1.append(riesgos)
        
    elif edad>50 and edad<=75:
        nombres2.append(nombre)
        riesgo2.append(riesgos)
        
    elif edad<=50:
        nombres3.append(nombre)
        riesgo3.append(riesgos)
        
    linea=arch.readline().strip()
    

for a in range(len(riesgo1)-1):           # orden la tabla de los riesgos altos de menor a mayor
    for b in range(a+1,len(riesgo1)):
        if riesgo1[a]<riesgo1[b]:
            aux=riesgo1[a]
            riesgo1[a]=riesgo1[b]
            riesgo1[b]=aux
            
            aux2=nombres1[a]
            nombres1[a]=nombres1[b]
            nombres1[b]=aux2
            

for a in range(len(riesgo2)-1):           # orden la tabla de los riesgos medios de mayor a  menor en este caso
    for b in range(a+1,len(riesgo2)):
        if riesgo2[a]<riesgo2[b]:       # solo cambiamo el signo a  este <    
            aux=riesgo2[a]
            riesgo2[a]=riesgo2[b]
            riesgo2[b]=aux
            
            aux2=nombres2[a]
            nombres2[a]=nombres2[b]
            nombres2[b]=aux2
            

for a in range(len(riesgo3)-1):           # orden la tabla de los riesgos bajos de menor a mayor
    for b in range(a+1,len(riesgo3)):
        if riesgo3[a]<riesgo3[b]:
            aux=riesgo3[a]
            riesgo3[a]=riesgo3[b]
            riesgo3[b]=aux
            
            aux2=nombres3[a]
            nombres3[a]=nombres3[b]
            nombres3[b]=aux2
            
            
print("Riesgos Altos")
print("")
for a in range(len(nombres1)):
    print(f"{nombres1[a]} ({riesgo1[a]})")
print("")    
print("Riesgos Medios")
print("")
for a in range(len(nombres2)):
    print(f"{nombres2[a]} ({riesgo2[a]})")
print("")   
print("Riesgos Bajos")
print("")
for a in range(len(nombres3)):
    print(f"{nombres3[a]} ({riesgo3[a]})")
    
    
        
                       
