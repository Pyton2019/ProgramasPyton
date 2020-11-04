x=int(input("ingrese un numero: "))
y=int(input("ingrese otro numero: "))
if y==0:
    print("indeterminacion")
else:
    if x%y==0:
        print("el numero es entero")
    else:
        if x%y!=0:
            print("el numero no es entero")