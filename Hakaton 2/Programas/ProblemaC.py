# Team201
# Alexi Diaz
# Esteban Marin


def cambioMoneda(lista):
    for i in lista:
        if i == "B":
            Conversion = 1000
        if i == "M":
            Conversion=1
    Numero = lista[1:len(lista)-1]
    Numero = float(Numero)
    Valor = Numero*Conversion
    return Valor





def ordenar(lista1,columna,matriz):
    for a in range(len(lista1)-1):
        for b in range(a+1,len(lista1)):
            if matriz[a,columna] < matriz[b,columna]:
                aux = matriz[a,columna]
                matriz[a,columna] = matriz[b,columna]
                matriz[b,columna] = aux
                
                aux = lista1[a]
                lista1[a] = lista1[b]
                lista1[b]= aux



def suma(matriz):
    Sumas = []
    for a in range(13):
        Suma = 0
        for b in range(13):
            Suma+=matriz[a,b]
        Sumas.append(Suma)
    return Sumas

def esta(elemento,lista):
    if elemento in lista:
        lista.remove(elemento)
    return lista


import numpy as np
matrixx=np.zeros([13,13])

arch = open("stocks.txt","r",encoding="utf-8")
linea=arch.readline().strip()
omi=0
total=0
categorias=[]
sectores=[]
while linea!="":
    partes=linea.split(";")
    empresa=partes[0]
    valorizacion=partes[1]
    sector=partes[2]
    categoria=partes[3]
    total+=1
    if empresa == "n/a" or valorizacion == "n/a" or sector == "n/a" or categoria == "n/a":
        
        omi+=1
        
        
    if categoria not in categorias and categorias != "n/a" and empresa!="n/a" and sector!="n/a" and valorizacion!="n/a":
        categorias.append(categoria)
        
    if sector not in sectores and sectores != "n/a" and categoria !="n/a" and empresa!="n/a"and valorizacion!="n/a":
        sectores.append(sector)
    if valorizacion !="n/a" and sector!="n/a" and categoria!="n/a" and empresa!="n/a":
        
        valor=cambioMoneda(valorizacion)
       
        f=categorias.index(categoria)
        c=sectores.index(sector)
        matrixx[f][c]+=valor
    esta("n/a",categorias)
    esta("n/a",sectores)
        
    linea=arch.readline().strip()

sum_sector=suma(matrixx)
mayor=-1
nomMayor=""

for a in range(len(sum_sector)):
    if sum_sector[a] > mayor:
        mayor = sum_sector[a]
        nomMayor = categorias[a]
        
ColumnaMayor = sectores.index(nomMayor)
ordenar(categorias,ColumnaMayor,matrixx)
print(omi,"datos omi de",total)
print("Mayor es",nomMayor)

for i in range (len(categorias)):
    print("Cat",categorias[i],round(matrixx[i,ColumnaMayor],2))

