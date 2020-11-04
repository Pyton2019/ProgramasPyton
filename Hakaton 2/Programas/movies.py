import numpy as np

matriz=np.zeros([20,20])

archive=open("movies.txt","r",encoding="utf-8")
linea=archive.readline().strip()


sexo=[]
categorias=[]

           

while linea!="":
    partes=linea.split(";")
    #sexo=partes[0]
    #categorias=partes[1]
    #pelicula=partes[2]
    #cantidad_Espectadores=partes[3]
    
    if partes[0] not in sexo:
        sexo.append(partes[0])
        
    catego=partes[1].split("|")
    
    for i in range(len(catego)):
        
        if catego[i] not in categorias:
            categorias.append(catego[i])
    
        x=categorias.index(catego[i])
        y=sexo.index(partes[0])
        matriz[x][y]+=float(partes[3])
        
            
    linea=archive.readline().strip()
    
categoria_H=""
categoria_M=""  
 
mayor=-999999
menor_M=999999 

for col in range(len(sexo)):
    for fil in range(len(categorias)):
        if sexo[col]=="Female":
            if  matriz[fil][col]<menor_M:
                menor_M= matriz[fil][col]
                categoria_M=categorias[fil]
                
          
        
        if sexo[col]=="Male":
            if matriz[fil][col]>mayor:
                mayor= matriz[fil][col]
                categoria_H=categorias[fil]
categoria_to=""                
mayor_todos=-9999999    
for fil in range(len(categorias)):
    suma=0
    for col in range(len(sexo)):
        
        suma+=matriz[fil][col]
        
    if suma>mayor_todos:
        mayor_todos=suma
        categoria_to=categorias[fil]
        
                
          
print("La categoria mas vista por hombres es",categoria_H,"con",mayor,"espectadores")
print("La categoria menos vista por mujeres es",categoria_M,"con",menor_M,"espectadores")  
print("La categoria mas vista por todos es",categoria_to,"con",mayor_todos,"espectadores")      
            
        
       
   
    
    

