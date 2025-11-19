# Realiza un programa que gestione un establecimiento de venta de bocadillos. Un pedido se 
#compone de: bocadillo, acompañamiento y bebida. Un cliente puede pedir más de un pedido. El 
#dependiente a partir del menú (ver imagen), se encarga de introducir los datos. El menú solo se 
#visualiza una vez al ejecutar el programa. El programa debe preguntar al dependiente tras la 
#realización de un pedido, si quiere gestionar otro. 
#El establecimiento contempla los siguientes descuentos:
#Si el total a pagar es entre 20 y 30 euros, se aplica un descuento del 5%
#Si el total a pagar es superior a 30 euros, se aplica un descuento del 15%
#Una vez se finaliza la introducción de todos los pedidos de un cliente, debe aparecer por pantalla:
#• El número de pedidos realizados
#• Total a pagar.
#• Total con IVA (10%)
#• Total con el descuento aplicado.


#MENÚ
#1. Bocadillo de calamares- 9 €"
#2. Bocadillo de chistorra - 4.5 €
#3. Bikini de jamón - 2.5 €"
#ACOMPAÑAMIENTO
#1. Patatas finas - 1.5 €
#2. Patatas gruesas - 1.75 €
#3. Patatas rústicas - 2 €
#BEBIDAS
#1. Coca cola - 2 €"
#2. Acuarius - 1.5 €
#3. Agua - 1 €"

print('***** MENÚ *****')
print('1. Bocadillo de calamares- 9 €')
print('2. Bocadillo de chistorra - 4.5 €')
print('3. Bikini de jamón - 2.5 €"')
print('***** ACOMPAÑAMIENTO *****')
print('1. Patatas finas - 1.5 €')
print('2. Patatas gruesas - 1.75 €')
print('3. Patatas rústicas - 2 €')
print('***** BEBIDAS *****')
print('Coca cola - 2 €')
print('Acuarius - 1.5 €')
print('Agua - 1 €')
np=1
precio=0
pf=0
s='si'
while s=='si':

    m=int(input('introduce el menu principal'))
    a=int(input('introduce el acompañamiento'))
    b=int(input('introduce la bebida'))
    if m == 1:
        precio+=9
    elif m==2:
        precio+=4.5
    elif m ==3:
        precio+=2.5
    else:
        print('error')

    if a== 1:
        precio+=1.5
    elif a==2:
        precio+=1.75
    elif a ==3:
        precio+=2
    else:
        print('error')
        
    if b== 1:
        precio+=2
    elif b==2:
        precio+=1.5
    elif b==3:
        precio+=1
    else:
        print('error')
    

    s=input('desea pedir otro menú si/no:')
    if s!='si':
        break
    else:
        np+=1

print('el total a pagar es de ',precio, 'euros')

piva=precio+precio*10/100
piva=round(piva, 2)
print('el total con el iva es de:',piva,'euros')
if precio >=20 and precio<=30:
    pf=piva-piva*5/100
    pf=round(pf, 2)
    print('como su pedido es entre 20 y 30 euros, aplicando 5% de descuento, el precio final es:',pf,'euros')
if precio>30:
    pf=piva-piva*15/100
    pf=round(pf, 2)
    print('como su pedido es superior a 30 euros, aplicando 15% de descuento, el precio final es:',pf,'euros')
print('en total ha pedido:',np,' numero/s de pedidos')



