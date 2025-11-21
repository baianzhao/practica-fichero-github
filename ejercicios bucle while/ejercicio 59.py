#Diseña un programa que “piense” un numero aleatorio entre 0 y 1000 para que nos pida que 
#intentemos adivinarlo. En cada intento, el programa nos dirá si el numero introducido es mayor o 
#menor del correcto. No utilices break para salir del bucle. Cuando se acierte el número debe 
#mostrarse por pantalla un mensaje y el número de intentos.

import random

nr=random.randint(0,1000)
print(f'pista:{nr}')
y=False
while y==False:
    rnn=int(input('introduce un numero del 0 al 1000'))
    if rnn>nr:
        print('el numero es mayor al numero')
    elif rnn<nr:
        print('el numero introducido es menor al numero')
    elif nr==rnn:
        print('HAS ACERTADO')
        y=True