#Introduce por teclado dos números y muestre por pantalla la siguiente información: cociente, resto y si el dividendo es par o impar.

num1=float(input('introduzca el dividendo'))
mun2=float(input('introduzca el divisor'))
resultado=num1/mun2
resto=num1%mun2
print('el cociente es: ',resultado)
print('el resto es: ',resto)
if resto==0:
    paroimpar=1
else:
    paroimpar=0
if paroimpar==1:
    print('el dividendo es par')
else:
    print('el dividendo es impar')