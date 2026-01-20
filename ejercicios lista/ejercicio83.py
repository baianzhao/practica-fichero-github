#83. Modifica el código del ejercicio anterior para que el programa permita repetir x partidas (hasta
#que el usuario lo decida). Tienes que controlar una puntuación de cada partida de la siguiente
#manera, si la palabra la aciertas a la primera son 8 puntos, si la aciertas a la segunda 7 puntos y así
#sucesivamente.
#Una vez el usuario desea finalizar el programa tiene que sumar todas tus puntuaciones obtenidas.
#Si el total supera la media de la puntuación posible de todas las partidas, se puede decir que la
#suerte le acompaña, de lo contrario mejor no Se dediques a los juegos de azar . PISTA.. ¿existe
#algún método que permita sumar el contenido de una lista?
print('tendras que adivinar una de las palabras siguientes: casa,barco,gato,perro,madera,agua,puente,pantalón')
import random as rd
n=rd.randint(0,7)
v='casa,barco,gato,perro,madera,agua,puente,pantalón'
lista=v.split(',')
psecreta=(lista[n-1])
sino=False
pp=8
part ='si'
npart=0
pt=[]
while part=='si':
    npart+=1
    psecreta=(lista[n-1])
    sino=False
    pp=8
    while sino==False:
        pintroducida=input('introduce una palabra')
        if psecreta==pintroducida:
            sino=True
            print('ACERTASTE')
            print('puntuacion actual:',pp)
            part=input('desea continuar? si/no')
            pt.append(pp)
        else:
            print('SIGUE JUGANDO')
            if pp==0:
                pp==pp
            else:
                pp-=1

ptotal=0
for x in pt:
    ptotal+=x

print(pt)
print('tu puntuacion final es de:',ptotal)
print('la media de las partidas realizadas es de:',npart*4)
if ptotal>npart*4:
    print('LA SUERTE TE ACOMPAÑA!!')
elif ptotal<npart*4:
    print('BOTSITADA HISTORICA!!!')
elif ptotal== npart*4:
    print('has hecho lo justo...')
