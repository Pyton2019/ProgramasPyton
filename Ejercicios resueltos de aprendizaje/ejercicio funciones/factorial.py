# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 11:12:55 2019

@author: alexi
"""


def factorial(x):
    cont=1   #variable que guardara el factorial
    for i in range(x,0,-1):
        cont=cont*i
    return cont

d=int(input("ingrese un numero: "))
p=factorial(d)
print(d,"!","=",p)
        