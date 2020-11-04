x=int(input("ingrese un numero: "))
y=int(input("ingrese otro numero: "))
if y==0:
    print("indeterminacion")
else:
    if x%y==0 and x>y:
        print("el numero es entero") 
        print("numero mayor: "+str(x))
        print("numero menor: " +str(y))
        print("numero mayor multiplo del numero menor")
    else:
        if x%y==0 and x==y:
            print("el numero es entero")
            print("los numeros son iguales a: "+str(x))
        else:   
            if x%y!=0 and x<y:
                print("el numero no es entero")
                print("resto: "+str(x%y))
                print("numero mayor: "+str(y))
                print("numero menor: "+str(x))
                print("numero mayor no es multiplo del numero menor")
            else:
                if x%y!=0 and x>y:
                    print("el numero no es entero")
                    print("resto: "+str(x%y))
                    print("numero mayor: " +str(x))
                    print("numero menor: "+str(y))
                    print("numero mayor no es multiplo del numero menor")
       

  