
nom=[]  #nombre de participantes
sex=[]#sexo del participante
tie=[] # tiempo en que demoro en completar la carrera
sumador=0 #sumador tiempo carrera hombres
contador=0  #contador cuantos participantes hombres hay
sumadorf=0
contadorf=0 
menor=999999 #menor tiempo de carrera
nombre=""
d=int(input("Cuantos participantes tiene la carrera: "))
for i in range(d):
    nom.append(input(f"Nombre del participante {i+1}: "))
    sex.append(input(f"Sexo del participante {nom[i]}: "))
    tie.append(int(input(f"Tiempo en que demoro en completar la carrera {nom[i]}: ")))
    
    if sex[i]=="masculino":
        sumador=sumador+tie[i]
        contador=contador+1
    if sex[i]=="femenino":
        sumadorf=sumadorf+tie[i]
        contadorf=contadorf+1
        
    if tie[i]<menor:
        menor=tie[i]
        nombre=nom[i]
        
promediom=sumador/contador
promediof= sumadorf/contadorf

print("El promedio de tiempo de carrera para hombres es de",promediom,"minutos")
print("El promedio de tiempo de carrera para mujeres es de",promediof,"minutos")
print("El menor tiempo de carrera fue para",nombre,"con",menor,"minutos")
        
  
 
    
    
