"""
x=float(input("nota 1: "))
y=float(input("nota 2: "))
z=float(input("nota 3: "))
p=float(input("nota prueba corta 1: "))
f=float(input("nota prueba corta 2: "))
r=float((p+f)/2)

a=x*0.2
b=y*0.3
c=z*0.4
d=r*0.1
e=(a+b+c+d)*0.7
t=float(input("nota taller: "))
g=t*0.3
h=(t+0.3)*0.3
u=int(input("numeros integrantes del taller: "))
if u==2:
    print("nota final: %s",str(e+h))
else:
    if u==3:
        print("nota final: %s",str(e+g))

"""
y=input("dime nombre: ")
e=int(input("dime edad: "))
f=float(input("indique peso (kg): "))
while(e<0 or f<0):
        if(e<0):
            print("Edad incorrecta \ningrese una valida")
            e=int(input("ingrese edad: "))
        else:
            print("Peso incorrecta \ningrese un peso valida")
            f=float(input("ingrese peso: "))
            

if(e>=18 and f>100):
    print("Su nombre es %s usted es mayor de edad dado que tiene %d años y tiene un sobrepeso ya que su peso es %f"%(y,e,f))

else:
    print("Su nombre es %s usted es menor de edad dado que tiene %d años y pesa %f"%(y,e,f))
        
