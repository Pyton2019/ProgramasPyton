# -*- coding: utf-8 -*-

def agregar(nombres):
    arch=open("archivo.txt","r")      #lectura de un archivo
    linea=arch.readline().strip()
    while linea!="":
        nombres.append(linea)          #agrega los elementos de cada linea del archivo a la lista
        linea=arch.readline().strip()
    arch.close
        

lista=[]
agregar(lista)
print(lista)


