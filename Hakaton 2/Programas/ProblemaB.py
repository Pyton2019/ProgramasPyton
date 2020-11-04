#team 201 
#Alexi Diaz 
#Esteban Marin

import numpy as np
meses = ['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre']
ciudades = []
archivo = open("ventas.txt", 'r', encoding='utf-8')
linea=archivo.readline().strip()
while linea!= "":
    parte = linea.split(",")
    c = 1
    horass = False
    for numeros in parte[2].split(":"):
        numeros = int(numeros)
        if c == 1:
            if numeros >= 8 and numeros <= 17:
                horass = True
        c += 1
    if horass == True:
        if parte[0] not in ciudades:
            ciudades.append(parte[0])
    linea=archivo.readline().strip()
matriz = np.zeros([len(ciudades),len(meses)])
archivo.close
archivo = open("ventas.txt", 'r', encoding='utf-8')
linea = archivo.readline().strip()
l=0
no=0
while linea!= "":
    parte = linea.split(",")
    ciudad = parte[0]
    ventas = float(parte[1])
    hora = parte[2]
    mes = parte[3]
    c = 1
    horass = False
    minutos = False
    for numeros in hora.split(":"):
        numeros = int(numeros)
        if c == 1:
            if numeros >= 8 and numeros <= 17:
                horass = True
        if c == 2:
            if numeros <= 59:
                minutos=True
        c += 1
    l+=1
    if horass == True and minutos == True: # a esta hora
        no+=1
        f=ciudades.index(ciudad)
        c=meses.index(mes)
        matriz[f][c]+=ventas
    linea = archivo.readline().strip()
for x in range(len(meses)):
    s=0
    for y in range(len(ciudades)):
        s+=matriz[y][x]
    print(meses[x],s)
for x in range(len(ciudades)):
    print(ciudades[x],round(sum(matriz[x])/len(matriz[x]),2))
print("porcentaje",(1-(no/l))*100,"%")
