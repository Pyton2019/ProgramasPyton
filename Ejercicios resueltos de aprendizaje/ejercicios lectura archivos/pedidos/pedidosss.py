# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 20:37:00 2019

@author: alexi
"""

arch=open("pedidos.txt","r")#alexi diaz vergara
linea=arch.readline().strip()
estado1=""

while linea!="":
    partes=linea.split(",")
    ndespacho=int(partes[0])#numero de despacho
    origen=partes[1]#ciudad de origen
    destino=partes[2]#ciudad de destino
    numero=int(partes[3])#numero de estados
    registro=int(partes[4])#dia creacion del registro
    estadosvalidos=0
    total=0#total estado
    nommax=""#nombre estado maximo
    nommin=""#nombre minimo
    maximo=-999999
    minimo=999999
    dife=0  #diferencia edad
    for i in range(numero):
        linea=arch.readline().strip()
        parte=linea.split(",")
        estado=parte[0]#nombre estado despacho
        dia= int(parte[1])#dia en que fue despachado
        total+=1
        
        d=dia-registro #diferencia
        if dia>=registro:
            if dia>maximo:
                maximo=dia
                nommax=estado
                diferencia=d
            estadosvalidos=estadosvalidos1
    print(nommax,d)
            
            
    print (estadosvalidos,"(",total,")") 
            
        
            
            
        
    linea=arch.readline().strip()
