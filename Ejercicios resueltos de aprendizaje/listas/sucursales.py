sucursal=[]
ingresos=[]
d=int(input("cuantas sucursales tiene la empresa: "))
conin=0  #contador de ingresos
menor=999999999999  #sucursal menor ingresos
nombrem="" #nombre sucursal con menores ingresos
mayor=-999999 # sucursal con mayores ingresos
nombrema="" #nombre de la sucursal con mayor ingresos
for i in range(d):
    sucursal.append(input("nombre de la sucursal: "))
    
    ingresos.append(int(input(f"cuantos ingresos genero {sucursal[i]}: ")))  #poner f delandte de entrecomilla para preguntar con el nombre de la sucursal anterior.
    conin=conin+ingresos[i]
    if ingresos[i]<menor:
        menor=ingresos[i]
        nombrem=sucursal[i]
    if ingresos[i]>mayor:
        mayor=ingresos[i]
        nombrema=sucursal[i]
print("El ingreso total de la empresa fue: ",conin)
print("La sucursal con menores ingresos es: ",nombrem,"con","$",menor)
print("La sucursal con mayores ingresos es: ",nombrema,"con","$",mayor)