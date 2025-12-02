#Programa que pida continuamente números por teclado hasta que el usuario introduzca el valor
#-99. Por pantalla debe aparecer cuál de todos los números introducidos es el mayo y cuál el menor.

tpar=0
ti=0
tpos=0
tn=0
tc=0
ts=0
lista=[]

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

        lista.append(valor)
    
        ts=ts+valor
print('RESUMEN')
print(f'el numero de pares es {tpar}')
print(f'el numero de impares es {ti}')
print(f'el numero de positivos es {tpos}')
print(f'el numero de negativos es {tn}')
print(f'el total es {ts}')
print(f'el numero mayor es {max(lista)}')
print(f'el numero menor es {min(lista)}')