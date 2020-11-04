# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 10:47:57 2019

@author: alexi
"""

def esprimo(x):
    cont=0
    for i in range(x,0,-1):
        if x%i==0:
            cont=cont+1
    if cont==2:
        print(x)
    
    
    
for i in range(3,101):
    f=esprimo(i)
