# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 19:27:17 2019

@author: alexi
"""
multiplicador=1
print("calculador de factorial")
x=int(input("Dame un numero: "))
while x<0:
    print("numero no valido, ingreselo de nuevo")
    f=int(input("Dame un numero: "))
    x=f
for i in range(1,x+1):
    multiplicador=multiplicador*i
print("El factorial de "+str(x))
print(multiplicador)

    
    
    
    