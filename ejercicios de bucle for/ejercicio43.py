# Realiza un programa que recorra con un for una palabra introducida por teclado y se imprima por pantalla cada letra
pal=input('introduce una palabra')
pos=0
for a in pal:
    print('En la posición ',pos, 'está la ',a)
    pos+=1
    
