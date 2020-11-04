#Haga un programa que, 
#dado un numero n ingresado por pantalla, imprima una lista con todos los números desde n hasta 0. 
#La lista debe llenarse DENTRO de una función.


def funcion(lista):
    n=int(input("Ingrese un numero: "))
    for i in range(n,-1,-1):
        lista.append(i)
        
        
    
l1=[]      # creamos variable lista
x=funcion(l1) # aqui retonrna cada valor agregado de la funcion
print(l1)
    