
car=[]# cargas familiares
edad1=[]
sueldo_base=[]
rut=[]
nombre=[]
region=[]
sexo=[]
tipo=[]
sueldof=[]#sueldo final
  
n=int(input("Cuantos personas son: "))
for i in range(n):
        

    rut.append(int(input("Rut de usuario sin digito verificador: ")))   
    nombre.append(input("Ingrese nombre: "))
    sexo.append(input(f"sexo de {nombre[i]}: "))
    sueldo_base.append(int(input("Ingrese sueldo base: ")))
    tipo.append(input("Ingrese tipo (senador-diputado): "))
    region.append(input("Ingrese region: "))
    car.append(int(input("ingrese numero de cargas familiares: ")))
   

    
  
    if tipo[i]=="diputado":
        asig=0 #asignacion segun la region para diputado 
        if region[i]=="II" or region[i]=="IV" or region[i]=="VI" or region[i]=="VIII" or region[i]=="X" or region[i]=="XII":
            asig=580000
        else:
            asig=575000
    bono=0#bono cargas familiares para diputado
    rut1=[]
    edad1=[]
    for r in range(car[i]):
        rut1.append(int(input("Ingrese rut de la carga: ")))
        edad1.append(int(input("ingrese edad de la carga: ")))
        if edad1[r]<=2:
                bono=bono+55000
        if edad1[r]>2 and edad1[r]<=21:
                bono=bono+30000
        if edad1[r]>21:
                bono=bono+0
    if tipo[i]=="senador":
        asig=0 #asignacion segun la region senador
        if region[i]=="I" or region[i]=="II" or region[i]=="III" or region[i]=="IV" or region[i]=="XV":
            asig=0.05*sueldo_base[i]
        else:
            asig=0.04*sueldo_base[i]
            
            
    sueldof.append(bono+asig+sueldo_base[i])
    
con=0  #contador total sueldo diputado
co=0  #contador diputados  
c=0 #contador senadores con sueldo mayor a $3.000.000 
tota=0  #contador total de senadores  
contaaa=0   #contador diputados con mas de 5 cargas familiares
corr=0 #contador senadores con mas de 5 cargas familiares 
menor=999999999 #menor sueldo de diputados  
nombre1="" #nombre del diputado con menor sueldo y al menos 1 carga familiar
for i in range(n):
      if tipo[i]=="senador":
          if sueldof[i]>=3000000:
              c=c+1
          if car[i]>4:
              corr=corr+1
          tota=tota+1
          print("El sueldo del senador",nombre[i],"es","$",sueldof[i])
     
      if tipo[i]=="diputado":
          con=con+sueldof[i]
          co=co+1
          if car[i]>4:
              contaaa=contaaa+1
          if car[i]>0:
              if sexo[i]=="masculino":
                  if sueldof[i]<menor:
                      menor=sueldof[i]
                      nombre1=nombre[i]
          print("El sueldo del diputado",nombre[i],"es","$",sueldof[i])
if co!=0:   #condicional por si no hay diputados ,no se imprima nada      
    print("El promedio de sueldos de los diputados es: ",con/co)
if c!=0:    #condicional por si no hay senadores, no se imprima nada
    print("Porcentaje de senadores con respecto al total con sueldo mayor a $3.000.000 es: ",(c*100)/tota,"%")
if contaaa!=0:
    print("Numero de diputados con mas de 5 cargas familiares: ",contaaa)
if corr!=0:
    print("Numero de senadores con mas de 5 cargas familiares: ",corr)
if menor!=999999999:
    print("El diputado con menor sueldo y al menos una carga familiar es: ",nombre1)
          
          
        
        
  
    
        
  
    
    
    
        
            
    
            
            
        
        