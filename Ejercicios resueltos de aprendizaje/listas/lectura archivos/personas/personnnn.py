# Haga un programa leyendo "Personas.txt"que ingrese por pantalla el nombre y edad de "n" personas 
#(n también debe ser ingresado por pantalla) y luego imprima la lista de nombres y edades.


nombree=[]
edadd=[]
rutt=[]
arch=open("Personas.txt","r")
linea=arch.readline().strip()
while linea!="":
    parte=linea.split(",")
    rut=(parte[0])
    nombre=parte[1]
    edad=int(parte[2])
    
    nombree.append(nombre)
    edadd.append(edad)
    rutt.append(rut)
    
    linea=arch.readline().strip()
    
print(nombree)
print(rutt)
print(edadd)
    
