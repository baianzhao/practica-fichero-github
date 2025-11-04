#Programa que pida n números y que, tras introducir el último número, debe aparecer por 
#pantalla el número total de positivos, negativos y número de 0.
n=int(input('introduce el numero de numeros que quiere introducir'))
pos=0
neg=0
zero=0
for num in range(n):
    nu=float(input('introduce un numero'))
    if nu>0:
        pos=pos+1
    elif nu<0:
        neg=neg+1
    elif nu ==0:
        zero=zero+1
print('la cantidad de numeros positivos es: ',pos)
print('la cantidad de numeros negativos es: ',neg)
print('la cantidad de ceros es: ',zero)