arch=open("plantacionpaltos.txt","r")
linea=arch.readline().strip()

sumador=0
mayor=0  #correspondiente a la mayor produccion
nombrem="" #nombre del arbol con mayor produccion
idem=""
edadm=0
altm=0
injermv=""
prtinje=0  #produccion total imnjertados
prtninje=0 #produccion total no injertados
sedad=0  #suamdor de edades
cedad=0  #contador de eedades para ver el total
sedadh=0  #sumador edad de hass
cedadh=0  #contador de edad de hass
sedade=0  #sumador edad de edranol
cedade=0  # contador edad edranol
sedadn=0  #sumador edad negra
cedadn=0  #contador edad negra
total1=0  #contador arboles con produccion mayor a $10.000
while linea!="":
    partes=linea.split(",")
    ide=(partes[0])#numero identificador del arbol
    raza=partes[1] #raza del arbol 
    pr18=int(partes[2])#produccion año 2018
    edad=int(partes[3])#edad del arbol
    alt=int(partes[4])#altura del arbol
    injer=partes[5]#si dice true esta injertado, false no esta injertado
    
    if pr18>10000:
        total1+=1
        
    if raza=="hass":
        sedadh=sedadh+edad
        cedadh=cedadh+1
    if raza=="edranol":
        sedade=sedade+edad
        cedade=cedade+1
    if raza=="negra de la cruz":
        sedadn=sedadn+edad
        cedadn=cedadn+1
        
    if edad>cedad:
        sedad=sedad+edad
        cedad=cedad+1
    
    if injer=="True":
        injermv="True"
        prtinje=prtinje+pr18
        
    if injer=="False":
        injermv="False"
        prtninje=prtinje+pr18
   
    sumador=sumador+pr18
    if pr18>mayor:
        mayor=pr18
        nombrem=raza
        idem=ide
        edadm=edad
        altm=alt
  
        
    linea=arch.readline().strip()
print("La produccion total es de: ",sumador)
print("Mayor produccion: ",idem,nombrem,"$",mayor,edad,"años",altm,"m",injermv)
if prtinje>prtninje:
    print("Los arboles injertados producen mas")
else:
    print("Los arboles no injertados producen mas")
promedio=sedad/cedad  # promedio de edades de todos los arboles
promedioh=sedadh/cedadh # promedio edad de raza hass
promedioe=sedade/cedade # promedio edad de raza edranol
promedion=sedadn/cedadn #promedio edad raza negra
print("Edad promedio raza negra de la cruz: ",promedion,"años")
print("Edad promedio raza edranol: ",promedioe,"años")   
print("Edad promedio raza hass: ",promedioh,"años")
print("Edad promedio de todos los paltos es: ",promedio,"años")
print(total1,"arboles con produccion mayor a $10.000")
