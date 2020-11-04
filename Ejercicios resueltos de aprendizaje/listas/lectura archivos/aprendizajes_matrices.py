
import numpy as np               # comando para crear matrices da lo mismo el nombre el np se puede cambiar y lo cambias al crear la matriz igual
lista=[2,3,4]
matriz=np.zeros([3,4]) #     np.zeros([filas x columnas])     la primera posicion es 0,0 la segunda 0,1 ...

matriz[0,0]=10              # cambiar los valores de las posiciones correspondientes en este caso primera posiciom
matriz[2,3]=20                # ultima posicion

lista[0]=4
lista[2]=200 

print(matriz)
print(lista)

print(matriz[2,3])   # imprimir elementos en particular
print(lista[1])