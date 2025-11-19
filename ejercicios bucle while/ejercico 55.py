# Última vez que reutilizamos el mismo código.. lo prometo . A partir del programa anterior 
#haz que sea todo exactamente igual pero teniendo en cuenta que el programa se repita siempre y 
#cuando la suma acumulada sea superior a 50 o la suma acumulada sea par. Con While

si=True
tts=0
v=1
while si== True:
    n1=int(input('introduce un numero'))
    n2=int(input('introduce un numero'))
    total=n1+n2
    tts=tts+total
    print(f'el resultado de la suma es: {n1+n2}')
    
    if tts>50 and tts%2!=0:
        si=False
    elif tts<50:
        si=True
        v+=1
print('programa finalizado')
if v==1:
    print(f'el total de la suma es: {tts} y en total lleva 1 operación realizada')
else: 
    print(f'el total de la suma es: {tts} y en total lleva {v} operaciones realizadas')