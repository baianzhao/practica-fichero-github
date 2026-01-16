#82. Modifica el programa anterior para que sea el usuario intente adivinar la palabra escogida al
#azar de la lista, indicando si es correcto o no. El programa debe no finaliza hasta que no se adivine
#la palabra.

import random as rd
n=rd.randint(0,7)
v='casa,barco,gato,perro,madera,agua,puente,pantalón'
lista=v.split(',')
psecreta=(lista[n-1])
sino=False
while sino==False:
    pintroducida=input('introduce una palabra')
    if psecreta==pintroducida:
        sino=True
        print('ACERTASTE')
    else:
        print('SIGUE JUGANDO')



