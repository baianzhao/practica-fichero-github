#. Modifica el programa anterior y haz que se repita el ciclo automáticamente hasta que el total 
#de todas las sumas sea superior a 50, será entonces cuando el programa finalice. No hará falta 
#preguntar si deseas repetir la operación. En cada operación aparece por pantalla la suma de la 
#operación y su acumulado. Para aquellos de vosotros que os fijáis en los detalles, controlar que el 
#mensaje del acumulado es singular o plural.. . Con While


si=True
tts=0
v=1
while si== True:
    n1=int(input('introduce un numero'))
    n2=int(input('introduce un numero'))
    total=n1+n2
    tts=tts+total
    print(f'el resultado de la suma es: {n1+n2}')
    
    if tts>50:
        si=False
    elif tts<50:
        si=True
        v+=1
print('programa finalizado')
if v==1:
    print(f'el total de la suma es: {tts} y en total lleva 1 operación realizada')
else: 
    print(f'el total de la suma es: {tts} y en total lleva {v} operaciones realizadas')