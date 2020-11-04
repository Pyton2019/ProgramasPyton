# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 19:27:17 2019

@author: alexi
"""
arch=open("sucursales.txt","r")
linea=arch.readline().strip()
mayor1=0
mayoredad=0
sucursalmayor=""
nombremayor=""
totalpersonas=0
contadorrango1=0
ponderacionmenor=99999
sucursalmen=""
while linea!="":
        partes=linea.split(",")
        sucursal=partes[0]
        personas=int(partes[1])
        
        if personas>mayor1:
            mayor1=personas
            sucursalmayor=sucursal
        sumador=0
        
        for i in range(1,personas+1):
            linea=arch.readline().strip()
            partes=linea.split(",")
            nombre=partes[0]
            edad=int(partes[1])
            
         
            if edad>mayoredad:
                mayoredad=edad
                nombremayor=nombre
            if edad>=25 and edad<=30:
                contadorrango1=contadorrango1+1
            if edad==33:
                print(nombre,sucursal)
                
        sumador=sumador+edad
        promedio=(sumador/personas)
        print("Promedio de edad: " +str(promedio))
        ponderacion=((personas*10)+(promedio*0.5))
        if ponderacion<ponderacionmenor:
                ponderacionmenor=ponderacion
                sucursalmen=sucursal
            
               
                
                
        totalpersonas=totalpersonas+personas
        porcentaje=(contadorrango1/totalpersonas)*100
        print("Porcentaje edad 25-30 es: "+str(porcentaje),"%")
        
             
                        
         
            
    
        linea=arch.readline().strip()
        
print("Mayor cantidad empleados: " +str(sucursalmayor))
print("persona mayor: " +str(nombremayor))
print("La ponderacion menor: "+str(sucursalmen))
print(ponderacionmenor)