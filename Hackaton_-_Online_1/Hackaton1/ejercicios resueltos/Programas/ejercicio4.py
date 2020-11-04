#Alexi Diaz Vergara
#team301

def promedio(a,b) :
    x=(a/b)
    return x
def indice(a,b) :
    for i in range(0,len(b)) :
        if a==b[i] :
            return i

arch=open("convalidados.txt", "r", encoding="utf-8")
linea=arch.readline().strip()
CONTADOR_RE=0

CONTADORCC=0
CONTADOIN=0
cont=0

mayorIN=0
mejorIN=""
sumadorCC=0
listaramos=[]
Cont_ramos=[]
x=0
listaFinal=[]
listaA=[]
while linea!="" :
    part=linea.split(",")
    identidad=part[0]
    tipo=part[1]
    cantidad=int(part[2])
    sumaIN=0
    for i in range(cantidad):
        linea=arch.readline().strip()
        partes=linea.split(",")
        asignatura=partes[0]
        nota=int(partes[1])
        if tipo=="RE":
            listaramos.append(asignatura)
        elif tipo=="IN" :
            sumaIN+=nota
    promedioIN=promedio(sumaIN,cantidad)
    if promedioIN>mayorIN :
        mejorIN=identidad
        
    if tipo=="RE" :
        CONTADOR_RE+=1
        
        
    elif tipo=="CC" :
        CONTADORCC+=1
        sumadorCC+=cantidad
        
    else :
        CONTADOIN+=1
    cont+=1
    linea=arch.readline().strip()
    
porcentajeRE=100*promedio(CONTADOR_RE,cont)
porcentajeCC=100*promedio(CONTADORCC,cont) 
porcentajeIN=100*promedio(CONTADOIN,cont)

listaramos.sort()
listaA=list(set(listaramos))
listaA.sort()

print("Porcentaje Alumnos RE: "+str(porcentajeRE),"%")
print("Porcentaje Alumnos CC: "+str(porcentajeCC),"%")
print("Porcentaje Alumnos IN: "+str(porcentajeIN),"%")
print("")

print("Alumno IN con mejor promedio: "+mejorIN)
print("Promedio ramos CC: "+str(sumadorCC))
print("")
print("Asignaturas RE mas convalidadas:")
for i in range(len(listaA)):
    asign=listaA[i]
    for j in range(len(listaramos)):
        num=listaramos.count(asign)
    print(asign, num)
    

