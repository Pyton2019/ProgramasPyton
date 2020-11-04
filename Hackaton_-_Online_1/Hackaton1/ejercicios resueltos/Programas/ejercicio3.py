#Alexi Diaz Vergara
#  team301


arch=open("movilizaciones.txt","r", encoding='utf-8')
linea=arch.readline().strip()
while linea!="":
    partes=linea.split(",")
   
    region=partes[0]
    cant=int(partes[1]) #cantidades de ciudades en la ciudad
    
    total1=0  #sumador de personas de cada ciudad
    mayor1=-999999 
    nombre1=""  # ciudad con mayores personas en movilizaciones
    menor=999999
    nombre2=""  #ciudad con menor habitantes
    for k in range(cant):
        linea=arch.readline().strip()
        partes=linea.split(",")
        ciudad=partes[0]
        p=int(partes[1]) # cantidad de personas que fueron
        if p>mayor1:
            mayor1=p
            nombre1=ciudad
        if p<menor:
            menor=p
            nombre2=ciudad
            
        total1=total1+p
        
    
    print(region,total1/cant,nombre1,nombre2)
        
    linea=arch.readline().strip()
    
    
    
    
    
