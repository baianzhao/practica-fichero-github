#Realiza un programa que sume dos números enteros por teclado y presente el resultado por 
#pantalla. El programa preguntará si deseas o no repetir la operación. Con While

si=True

while si== True:
    n1=int(input('introduce un numero'))
    n2=int(input('introduce un numero'))
    print(f'el resultado de la suma es: {n1+n2}')
    sn=input('desea continuar s/n:')
    if sn=='n':
        si=False
    elif sn =='s':
        si=True
print('programa finalizado')

