# Alexi Diaz Vergara  
# team301
def calculando(x,y,z):
    if h>0:
        
        g=1
        for i in range(z,1,-1):# para calcular factorial
            g=g*i  
    
        operacion= (((x**y)*g)+(x*y*z))/z**2
        return operacion
    else:
        k="error"
        return k
        
r=int(input())
f=int(input())
h=int(input())
print(calculando (r,f,h))
