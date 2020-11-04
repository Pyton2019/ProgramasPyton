#Alexi Diaz Vergara
# team301
file = open("transacciones.txt","r",encoding='utf-8')
sumavisa = 0
cantvisa = 0
sumamaster = 0
cantmaster = 0
nom1 = []
usuVisa = []
usuMaster = []
mayor1clie = []
mayorGASTO = []
clientegasta = ""
clientegasto = 0
def indice(a,b):
    for i in range(0,len(b)):
        if a == b[i]:
            return i
linea=file.readline().strip()
while linea != "":
    partes = linea.split("-")
    nombre = partes[0]
    valorcompra = int(partes[1])
    divisa = partes[2]
    tarjeta = partes[3]
    nom1.append(partes[0])
    if divisa == "USD":
        conversion = int(valorcompra) * 773
    elif divisa == "EUR":
        conversion = int(valorcompra) * 860
    else:
        conversion = int(valorcompra)
    if tarjeta == "VISA":
        for i in nom1:
            if i not in usuVisa:
                usuVisa.append(i)
        cantvisa += 1
        sumavisa += conversion
        percapitavisa = sumavisa / len(usuVisa)
    if tarjeta == "MASTERCARD":
        for i in nom1:
            if i not in usuMaster:
                usuMaster.append(i)
        sumamaster += conversion
        percapitamaster = sumamaster / len(usuMaster)
    if nombre in mayor1clie:
        x = indice(nombre,mayor1clie)
        mayorGASTO[x] += conversion
    else:
        mayor1clie.append(nombre)
        mayorGASTO.append(conversion)
        

    linea=file.readline().strip()
for i in range(0,len(mayorGASTO)):
    if mayorGASTO[i] > clientegasto:
        clientegasto = mayorGASTO[i]
        clientegasta = mayor1clie[i]
print("Las compras per cápita con VISA fueron:",percapitavisa,"CLP")
print("Las compras per cápita con MASTERCARD fueron:",percapitamaster,"CLP")
print("La persona que más compró fue",clientegasta)
print("Su gasto fue de",clientegasto,"CLP")
