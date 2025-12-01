#64. Programa que pida continuamente números por teclado hasta que el usuario introduzca el valor
#-99. Será entonces cuando por pantalla aparecerán las siguientes estadísticas:
#a) total de pares
#b) total de impares
#c) total de números positivos
#d) total de números negativos
#e) total de ceros
#f) total de la suma de todos los números introducidos

tpar=0
ti=0
tpos=0
tn=0
tc=0
ts=0

valor=0
while valor!=-99:
    valor=int(input('introduce un valor'))
    
    if valor==-99:
        break
    else:
    #par o impar
        if valor%2==0:
            tpar+=1
        elif valor%2!=0:
            ti+=1
    #mayor, menor o igual que 0.
        if valor<0:
            tn+=1
        elif valor>0:
            tpos+=1
        elif valor==0:
            tc+=1

        ts=ts+valor
print('RESUMEN')
print(f'el numero de pares es {tpar}')
print(f'el numero de impares es {ti}')
print(f'el numero de positivos es {tpos}')
print(f'el numero de negativos es {tn}')
print(f'el total es {ts}')