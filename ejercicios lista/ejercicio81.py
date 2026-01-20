#81. A partir de una lista definida, busca el método apropiado para que se visualice un valor de la
#lista al azar

import random as rd
n=rd.randint(0,7)
v='casa,barco,gato,perro,madera,agua,puente,pantalón'
lista=v.split(',')
print(lista[n-1])
