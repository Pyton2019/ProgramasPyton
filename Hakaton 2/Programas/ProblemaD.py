#team 201
#Alexi Diaz
#Esteban Marin
import numpy as np
l=0
letras=['A','B','C','D','E','F','G','H']
numeros=[1,2,3,4,5,6,7,8]
mapa1,mapa2 = np.zeros([8,8]),np.zeros([8,8])
archivo=open("battle.txt", 'r', encoding='utf-8')
linea=archivo.readline().strip()
while linea!="":
    l+=1
    if l<=16:
        parte=linea.split("-")
        if l<=8:
            for x in range(len(parte)):
                mapa1[l-1][x]+=int(parte[x])
        else:
            for x in range(len(parte)):
                mapa2[l - 9][x] += int(parte[x])
    linea = archivo.readline().strip()
archivo=open("battle.txt", 'r', encoding='utf-8')
linea=archivo.readline().strip()
l=0
ptj1=0
ptj2=0
ganador=""
s1, s2 = 0, 0
while linea!="":
    parte=linea.split(",")
    l+=1
    if l>16:
        letra1,numero1=parte[0][0],int(parte[0][1])
        letra2,numero2=parte[1][0],int(parte[1][1])
        if mapa2[numeros.index(numero1)][letras.index(letra1)]==1:
            ptj1+=1
            mapa2[numeros.index(numero1)][letras.index(letra1)]-=1
        if mapa1[numeros.index(numero2)][letras.index(letra2)]==1:
            ptj2+=1
            mapa1[numeros.index(numero2)][letras.index(letra2)] -= 1
    linea = archivo.readline().strip()
for x in range(8):
    for y in range(8):
        if mapa1[x][y] == 1:
            s2 += mapa1[x][y]
for x in range(8):
    for y in range(8):
        if mapa2[x][y] == 1:
            s1+= mapa2[x][y]
if s1==0:
    ganador="Jugador 1"
elif s2 == 0:
    ganador = "Jugador 2"
elif s2==s1:
    ganador="Empate"
elif ptj2>ptj1:
    ganador="Jugador 1"
elif ptj2>ptj1:
    ganador="Jugador 2"
print(ganador,"Gana")
