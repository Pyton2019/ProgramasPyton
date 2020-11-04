# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 14:18:33 2019

@author: alexi
"""

x=float(input("indique un numero: "))
y=float(x-(x/2)-(x/2))
z=x>((3+x)*4)
f=x>(x/3)    
if x==0:
    print("fin")
else:
        print(y)
        if x%2!=0 and (x>25 or x<-10):
            print("impar: "+str((3+x)*4))
        else:
            print(x/3)
            print("quiza es par")
        if x>z:
            print("intercambio: "+str(z))
        else:
            if x>f:
                print("intercambio: "+str(f))