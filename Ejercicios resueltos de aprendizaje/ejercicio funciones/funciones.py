# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 19:46:16 2019

@author: alexi
"""
def volumen(r):
    v1=4/3*3.14*r**3
    return v1





d=int(input("ingrese radio: "))
vo=0 #volumen esfera

if d>0:
    vo=volumen(d)  #retorna el valor de la funcion de arriba
    


    
print("el volumen de la esfera es: ",vo)
    
    


    