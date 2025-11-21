#Modifica el programa anterior para que tengas 3 intentos. Utiliza while

import random
rn=random.randint(1,5)
i=3
while i >0:
    n=int(input('introduce un numero del 1 al 5'))
    if rn==n:
        print('numero acertado')
    else:
        print('numero no acertado')
    i-=1