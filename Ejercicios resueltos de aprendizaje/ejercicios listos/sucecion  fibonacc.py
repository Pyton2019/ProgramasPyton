# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 19:55:21 2019

@author: alexi
"""

d=0
sumador=0
x=input("Elija producto: ").upper() 
if x=="A":
    k=270
    while d<k:
        n=int(input("ingrese monedas: "))
    
        while n!=100 and n!=50 and n!=10:
            print("ingrese valores validos")
            f=int(input("ingrese monedas: "))
            n=f
            
        sumador=sumador+n
        d=sumador
    if d==k:
        print("gracias por comprar el producto") 
    if d>k:
        print("espere el vuelto")
        
        
    
    
        
    
    


    
   
