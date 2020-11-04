arch=open("problema3.txt","r")
linea=arch.readline().strip()

while linea!="":
    partes=linea.split(",")
    num=int(partes[0])#numero de despacho
    origen=partes[1]#ciudad de origen
    destino=partes[2]#ciudad de destino
    cant=int(partes[3])#cantidad de estados
    diare=int(partes[4])#dia creacion del registro
    
    print(num,origen,destino,":")
    mayor=-983838 #diferencia para el mayor estado
    ulestado=""  #ultimo estado valido
    menor=99999999  #diferencia para el primer estado
    priestado=""  #primer estado valido
    dife1=0
    dife2=0
    for i in range(1,cant+1):
        linea=arch.readline().strip()
        partes=linea.split(",")
        estado=partes[0]  #estados 
        dia=int(partes[1])#dia cuando se realizo la operacion
        
        dife=dia-diare
        if dife>=0:
            if dife<menor:
                menor=dife
                priestado=estado
                dife1=dia-diare
            if dife>mayor:
                mayor=dife
                ulestado=estado
                dife2=dia-diare
    demora=dife2-dife1   
    print("Primer estado: ",priestado,"(",menor,")")
    print("Ultimo estado: ",ulestado,"(",mayor,")")
    print("Demora: ",demora)
        
    



            

    linea=arch.readline().strip()
