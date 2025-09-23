num1=False
while num1 != 34847214817866745235666666625326643575778478675634:
    num1=input('introduce un numero')
    siono=num1.isnumeric()
    if siono == True:
        print('si es numero')
        break
    elif siono == False:
        print('no es numero, vuelve a introducir')


