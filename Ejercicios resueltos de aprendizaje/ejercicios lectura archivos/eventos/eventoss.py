# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 19:16:46 2019

@author: alexi
"""

arch=open("eventos.txt","r")
linea=arch.readline().strip()
total=0
contadorperdida=0
ganancia2018=0
gananciamayor=0
perdidamayor=0

while linea!="":
    partes=linea.split(",")
    dia=int(partes[0])
    mes=int(partes[1])
    año=int(partes[2])
    nomevent=partes[3]
    inversion=float(partes[4])
    ingresos=float(partes[5])
    e=int(partes[6])
    f=int(partes[7])
    
    ganancia=ingresos-inversion
    atractividad=(e+2*f)/3
    exito=atractividad*1000+ganancia
    retencion=e-f
    print(dia,mes,año,nomevent,ganancia,retencion)
    
    
    if año==2018:
        ganancia2018=ganancia
        if ganancia<0:
            contadorperdida=contadorperdida+1   
        total=total+1
    if ganancia>gananciamayor:
        gananciamayor=ganancia
        nombremayor=nomevent
        dia1=dia
        mes1=mes
        año1=año
    if ganancia<perdidamayor:
        perdidamayor=ganancia
        nombremenor=nomevent
        dia2=dia
        mes2=mes
        año3=año
            
        
       
        
        
    linea=arch.readline().strip()
porcentajeperdida=(contadorperdida/total)*100
print("total eventos 2018: "+str(total))
print("ganancia 2018: "+str(ganancia2018))
print("perdida 2018 es: "+str(porcentajeperdida),"%")
print("evento con mayor ganancia:")
print(dia1,mes1,año1,nombremayor,gananciamayor)
print("el evento con mayor perdida es:")
print(dia2,mes2,año3,nombremenor,perdidamayor)
        
    

    
    
    
               