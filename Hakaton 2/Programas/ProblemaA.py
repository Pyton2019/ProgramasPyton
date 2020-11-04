# Team201
# Alexi Diaz
# Esteban Marin

arch = open("texto.txt",encoding = "utf-8")
linea = arch.readline().strip()
espacios =[]
puntos = []
comas = []
Aminusculas = []
Ominusculas = []
contadorespacios = 0
contadorpuntos = 0
contadorcomas = 0
contadorAminusculas = 0
contadorOminusculas = 0
while linea != "":
    for i in linea:
        if i == " ":
            contadorespacios += 1
    for i in linea:
        if i == ".":
            contadorpuntos += 1
    for i in linea:
        if i == ",":
            contadorcomas += 1
    for i in linea:
        if i == "a":
            contadorAminusculas += 1
    for i in linea:
        if i == "o":
            contadorOminusculas += 1
    operacion = contadorespacios * (contadorpuntos/contadorcomas) + (contadorAminusculas/contadorOminusculas)
    linea = arch.readline().strip()
print(round(operacion,2))