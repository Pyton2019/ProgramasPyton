# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 12:02:53 2019

@author: alexi
"""
nombre2=""
mayor2=-1
mayor=-1
nombre=""
x=input("ingrese nombre: ")
y=int(input("ingrese la edad aweonao: "))
while y>mayor:
    y=mayor
    nombre=x
while y<mayor:
    print("ingrese edad valida")
    f=int(input("ingrese la edad aweonao: "))
    if f>mayor:
        y=f
    nombre=x
       
r=input("ingrese otro nombre: ")
g=int(input("ingrese edad: "))
while g>mayor2:
    g=mayor2
    nombre=r
while g<mayor2:
    print("ingrese edad valida")
    d=int(input("ingrese la edad aweonao: "))
    if d>mayor2:
        g=d
    nombre=r
    
if mayor2>mayor:
    print("El mayor es:")
    print(nombre2)

else:
    mayor>mayor2
    print("El mayor es:")
    print(nombre)
      
    