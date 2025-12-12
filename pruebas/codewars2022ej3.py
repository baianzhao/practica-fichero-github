n1=int(input('nombre de productos'))
n2=int(input('nombre de cajas'))
n3=int(input('resto'))

if n1%n2==n3:
    print('correcto, la capacidad de cada caja es de:',n1/n2)
else:
    print('incorrecto')


