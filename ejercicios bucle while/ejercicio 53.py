#A partir del código anterior, haz que aparezca al finalizar el programa por pantalla el total las 
#sumas y el número de repeticiones. Con While

si=True
tts=0
v=0
while si== True:
    n1=int(input('introduce un numero'))
    n2=int(input('introduce un numero'))
    total=n1+n2
    tts=tts+total
    print(f'el resultado de la suma es: {n1+n2}')
    
    sn=input('desea continuar s/n:')
    if sn=='n':
        si=False
    elif sn =='s':
        si=True
        v+=1
print('programa finalizado')
print(f'el total de la suma es: {tts} y en total se ha repetido {v} veces')