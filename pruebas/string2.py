num1=False
a=0 #variable para determinar cuando romper el bucle
while a == 0:
    num1=input('introduce un numero')
    siono=num1.isnumeric()
    if siono == True:
        print('si es numero')
        a=1 #cuando el input es un numero, para de preguntar y se interumpe el bucle
    elif siono == False:
         print('no es numero, vuelve a introducir')
