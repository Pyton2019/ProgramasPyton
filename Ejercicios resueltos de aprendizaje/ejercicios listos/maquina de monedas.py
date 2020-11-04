# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 19:55:21 2019

@author: alexi
"""
f=0
c100b=0
c10b=0
c50b=0
c10=0
c50=0
c100=0
d=0
sumador=0
sumadorb=0
x=input("Elija producto: ").upper() 
if x=="A":
    k=270
    while d<k:
        n=int(input("ingrese monedas: "))
    
        while n!=100 and n!=50 and n!=10:
            print("ingrese valores validos")
            n=int(input("ingrese monedas: "))
            #n=f
            
        sumador=sumador+n
        d=sumador
    if d>k:
        vueltototal=d-k
        while vueltototal>=100:
            vueltototal=vueltototal-100
            c100=c100+1
            
        while vueltototal>=50:
            vueltototal=vueltototal-50
            c50=c50+1
            
        while vueltototal>=10:
            vueltototal=vueltototal-10
            c10=c10+1
        print("su vuelto es:")
        for i in range(0,c10+1,1):
            if i==0:
                i=0
            if i>0:
                print(10)
        for i in range(0,c50+1,1):
            if i==0:
                i=0
            if i>0:
                print(50)
        for i in range(0,c100+1,1):
            if i==0:
                i=0
            if i>0:
                print(100)
    if d==k:
        print("gracias por comprar este producto")

if x=="B":
    l=340
    while f<l:
        f=int(input("ingrese monedas: "))
        
        while f!=100 and f!=50 and f!=10:
            print("ingrese solo monedas de 100,10 o 50")
            po=int(input("ingrese monedas: "))
            f=po
            
        sumadorb=sumadorb+f
        f=sumadorb
    if f>l:
        vueltob=f-l
        while vueltob>=100:
            vueltob=vueltob-100
            c100b=c100b+1
                
        while vueltob>=50:
            vueltob=vueltob-50
            c50b=c50b+1
                
        while vueltob>=10:
            vueltob=vueltob-10
            c10b=c10b+1
        print("su vuelto es:")
        for i in range(0,c10b+1):
            if i==0:
                i=0
            if i!=0:
                print(10)
        for i in range(0,c100b+1):
            if i==0:
                i=0
            if i>0:
                print(100)
        for i in range(0,c50b+1):
            if i==0:
                i=0
            if i>0:
                print(50)
    if f==l:
        print("Gracias por su compra")
                
        
                
                    
           
        
    
    
        
    
    


    
   
