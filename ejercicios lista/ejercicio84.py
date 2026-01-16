#84. A partir de la lista definida en el ejercicio 81, haz que se visualice por pantalla una de las
#palabras, pero con todas sus letras desordenadas. El usuario tendrá que recolocar y acertar la
#palabra secreta. El usuario tendrá 3 oportunidades para adivinar la palabra. 


import random as rd
n=rd.randint(0,7)
v='casa,barco,gato,perro,madera,agua,puente,pantalón'
lista=v.split(',')
psecreta=(lista[n-1])
pal = list(psecreta)            
letras = [ch for ch in psecreta]
rd.shuffle(letras)
print(letras)
int=3
acc=0
while int >0:

    if int==0:
        break
    w=input('introduce la palabra')
    if w==psecreta:
        print('HAS ACERTADO!!')
        acc+=1
        break
    else:
        print('NO HAS ACERTADO')
        int-=1

if acc==0:
    print('eres tonto')
