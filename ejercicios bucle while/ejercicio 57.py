#57. Realiza un programa que permita adivinar un número comprendido entre 1 y 5. El programa 
#debe controlar si el usuario introduce un número no comprendido entre 1 y 5

import random
rn=random.randint(1,5)

n=int(input('introduce un numero del 1 al 5'))
if rn==n:
    print('numero acertado')
else:
    print('numero no acertado')