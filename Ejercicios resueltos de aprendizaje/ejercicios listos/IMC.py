# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 19:52:00 2019

@author: alexi
"""
imc=0
contadordesnutricion=0
contadornormal=0
contadorsobrepeso=0
contadorobeso=0
contador=0
ñ=1
t=int(input("numeros de estudiantes: "))
while ñ<t:
    x=input("nombre: ")
    y=int(input("edad: "))
    while y<=0:
        print("ingrese una edad valida")
        k=int(input("edad: "))
        y=k
    e=float(input("estatura en metros: "))
    while e<=0:
        print("ingrese estatura valida")
        m=float(input("estatura en metros: "))
        e=m
    f=float(input("peso en kilogramos: "))
    while f<=0:
        print("ingrese peso valido")
        b=float(input("peso en kilogramis: "))
        f=b
    r=f/e**2
    if r<18.50:
        imc=r
        contadordesnutricion=contadordesnutricion+1
        
    if 18.50<=r<25:
        imc=r
        contadornormal=contadornormal+1
        
    if 25<=r<30:
        imc=r
        contadorsobrepeso=contadorsobrepeso+1
    if r>=30:
        imc=r
        contadorobeso=contadorobeso+1
        
        
    contador=contador+ñ
    ñ=contador
porcentajedesnutricion=((contadordesnutricion/t)*100)
porcentajenormal=((contadornormal/t)*100)
porcentajesobrepeso=((contadorsobrepeso/t)*100)
porcentajeobeso=((contadorobeso/t)*100)

print("Porcentaje alumnos con desnutricion: " +str(porcentajedesnutricion))
print("Porcentaje alumnos con obesidad: " +str(porcentajeobeso))
print("Porcentaje alumnos con normalidad de peso: " +str(porcentajenormal))
print("Porcentaje alumnos con sobrepeso: " +str(porcentajesobrepeso))



      


     
     
        
