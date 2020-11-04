# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 11:24:54 2019

@author: alexi
"""

def AreaTriangulo(b,h):
    a1=b*h/2  #funcion para sacar area con los parametros dados
    return a1
def AreaRectangulo(l,p):
    a2=l*p
    return a2
def AreaCirculo(r):
    a3=r**2*3.14
    return a3





    
print("Figuras geometricas")
print("1","Triangulo")
print("2","Rectangulo")
print("3","Circulo")
f=int(input("Elija una opcion: "))
while f!=1 and f!=2 and f!=3:
   print("Ingrese un valor de las opciones")
   f=int(input("Elija una opcion: "))
      
if f==1:
    p=int(input("Ingrese Base: "))
    g=int(input("Ingrese Altura: "))
    area1=AreaTriangulo(p,g)
    print("El Area del Triangulo es: ",area1)
    
    
    
if f==2:
    ñ=int(input("Ingrese Largo: "))
    k=int(input("Ingrese Ancho: "))
    area2=AreaRectangulo(ñ,k)
    print("El area del Rectangulo es: ",area2)
if f==3:
    i=int(input("Ingrese Radio: "))
    area3=AreaCirculo(i)
    print("El area del Circulo es: ",area3)

        


