# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 17:41:53 2019

@author: alexi
"""
f=int(input("tamaño del mundo: "))
sumador=0
i=0
while i<f:
    
    print("se encuentra en la casilla: "+str(sumador))
p=i
q=int(input("longitud de cada salto: "))
n=int(input("cantidad de saltos: "))
i=p+(q*n)
sumador=sumador+i
    