# -*- coding: utf-8 -*-
arch=open("IMC.txt","r")
linea=arch.readline().strip()

def imc(x,a,b):
    i=a/b**2
    if i>=18.50 and i<24.99:
        print("imc entre 18.50-24.99: ",x,"con",i)
mayor=-99999
nombre1=""
while linea!="":
    partes=linea.split(",")
    nombre=partes[0]
    estatura=float(partes[1])
    peso=float(partes[2])
    imc1=imc(nombre,peso,estatura) #aqui retorna la funcion
    if estatura>mayor:
        mayor=estatura
        nombre1=nombre

    linea=arch.readline().strip()
print("la persona mas alta es: ",nombre1,"con",mayor,"metros")
