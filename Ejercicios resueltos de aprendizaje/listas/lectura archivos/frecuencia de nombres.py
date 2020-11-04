lista=[] # guardo los nombres
arch=open("nombres.txt","r")
linea=arch.readline().strip()
while linea!="":
    nombresss=linea
    lista.append(nombresss)
    
    linea=arch.readline().strip()


    
