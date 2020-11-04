# Haga un programa que ingrese por pantalla el nombre y edad de "n" personas 
#(n también debe ser ingresado por pantalla) y luego imprima la lista de nombres y edades.



nombre=[]
edad=[]
n=int(input("Ingrese numero de personas: "))
for i in range(n):
    nombre.append(input("Nombre: "))
    edad.append(int(input(f"Edad de {nombre[i]}: ")))
    
print(nombre)
print(edad)
    
