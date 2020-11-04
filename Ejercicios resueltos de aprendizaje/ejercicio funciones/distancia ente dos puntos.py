# -*- coding: utf-8 -*-

def distancia(x1,y1,x2,y2):
    f=((x2-x1)**2+(y2-y1)**2)**0.5
    print("DISTANCIA ENTRE LOS PUNTOS ES: ",f)#siempre poner el procedimiento (print o return) si no la varible queda indefinida
    



x1=int(input("Ingrese abscisa: "))
x2=int(input("Ingrese abscisa 2: "))
y1=int(input("Ingrese ordenada: "))
y2=int(input("Ingrese ordenada 2: "))

d=distancia(x1,y1,x2,y2)
