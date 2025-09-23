num1=False
a=0
while a == 0:
    num1=input('introduce un numero')
    siono=num1.isnumeric()
    if siono == True:
        print('si es numero')
        a=1
    elif siono == False:
        print('no es numero, vuelve a introducir')