#team 201
#Alexi Diaz Vergara
#Esteban Marin
import numpy as np
matriz=np.zeros([100,2])


arch=open("movies.txt","r",encoding='utf-8')
linea=arch.readline().strip()
sexos=["Male","Female"]
Genero=[]
generoMale=""
mayorMale=0
generoFemale=""
menorFemale=100000000000000000000
c=0
masVisto=0
s=0
generoMasVisto=""

while linea!="" :
    part=linea.split(";")
    sexo=part[0]
    y=sexos.index(sexo)
    generos=part[1]
    peli=part[2]
    cant=int(part[3])
    sepGenero=generos.split("|")
    for i in range (0,len(sepGenero)):
        genero=sepGenero[i]
        if genero not in Genero:
            Genero.append(genero)
        x=Genero.index(genero)
        matriz[x][y]+=cant

    linea=arch.readline().strip()

for i in range (0,len(Genero)):
    if matriz[i][0]>mayorMale:
        mayorMale=matriz[i][0]
        c=i
generoMale=Genero[c]

print("La categoría más vista por hombres es",generoMale,"con",int(mayorMale),"espectadores")

for i in range (0,len(Genero)):
    if matriz[i][1]<menorFemale:
        menorFemale=matriz[i][1]
        c=i
generoFemale=Genero[c]

print("La categoría menos vista por mujeres es",generoFemale,"con",int(menorFemale),"espectadores")

for i in range(0,len(Genero)):
    suma=matriz[i][0]+matriz[i][1]
    if suma>masVisto :
        masVisto=suma
        s=i
generoMasVisto=Genero[s]

print("La categoría más vista por todos es",generoMasVisto,"con",int(masVisto),"espectadores")