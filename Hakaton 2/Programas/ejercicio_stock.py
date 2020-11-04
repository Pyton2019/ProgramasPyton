
import numpy as np

matriz=np.zeros([20,20])
archivo=open("stocks.txt","r",encoding='utf-8')
linea=archivo.readline().strip()



def cambio(valor):
    for i in valor:
        if i=="B":
            conversion=1000
            
        elif i=="M":
            conversion=1
    numero=valor[1:len(valor)-1]
    numero=float(numero)
    valor=numero*conversion
              
    return valor

def ordenar(lista,lista2):  #ordenar de mayor a menor
    for a in range(len(lista)-1):
        for b in range(a+1,len(lista)):
            if lista[a]<lista[b]:
                aux=lista[a]
                lista[a]=lista[b]
                lista[b]=aux
                
                aux1=lista2[a]
                lista2[a]=lista2[b]
                lista2[b]=aux1
    
            
    
con_omitidos=0
empre=[]
valor1=[]
sect=[]
cate=[]
total=0
while linea!="":
    partes=linea.split(";")
    empresa=partes[0]
    valorizacion=partes[1]
    sector=partes[2]
    categoria=partes[3]
    
    if empresa=="n/a" or valorizacion=="n/a" or sector=="n/a" or categoria=="n/a":
        con_omitidos+=1
        
    if categoria not in cate and categoria!="n/a" and sector!="n/a" and valorizacion!="n/a" and empresa!="n/a":
        cate.append(categoria)
        
    if sector not in sect and categoria!="n/a" and sector!="n/a" and valorizacion!="n/a" and empresa!="n/a":
        sect.append(sector)
    
    if  categoria!="n/a" and sector!="n/a" and valorizacion!="n/a" and empresa!="n/a":
        

            valor1=cambio(valorizacion)
            f=cate.index(categoria)
            g=sect.index(sector)
            matriz[f][g]+=valor1
    total+=1   
    linea=archivo.readline().strip()
sect1=""  #mayor sector
categoria_M=[]  #categorias del sector mayor
valorizacion_M=[]
mayor=-999999
for col in range(len(sect)):
    suma1=0
    for fil in range(len(cate)):
        matriz[fil][col]+=suma1
        
    if suma1>mayor:
        mayor=suma1
        sect1=sect[col]
y=0
for i in range(len(cate)):        
    if sect1 in sect:
        x=sect.index(sect1)
        categoria_M.append(cate[i])
        valorizacion_M.append(matriz[y][x])
        y+=1
        


ordenar(valorizacion_M,categoria_M)

print(con_omitidos,"datos omitidos de",total)
print("Mayor es",sect1)
for i in range(len(categoria_M)):
    
    print("cat",categoria_M[i],round(valorizacion_M[i],2))


 
    
    
        





        
    
    

    
