print('Las 3 contraseñas deben de tener como minimo 3 numeros, 3 letras y 2 simbolos cada una')
for password in range(3):
    n=0
    l=0
    s=0
    cc=0
    lm=0
    lmi=0
    nmi5=0
    nmen5=0
    psw=input('introduce una contraseña')
    for caracter in psw:
        if caracter.isalpha()==True:
            l+=1
            if caracter.islower()==True:
                lmi+=1
            else:
                lm+=1
        elif caracter in '1234567890':
            n+=1
            if int(caracter)<5:
                nmen5+=1
            else:
                nmi5+=1

        else:
            s+=1
    if n<3 or l<3 or s<2:
        print('Error, la contraseña no cumple con los requisitos')
    else:
        print('la contraseña es correcta')
        cc+=1
    print(f'su contraseña tiene un total de {lm} letras mayusculas y {lmi} letras minusculas, un total de {l} letras')
    print(f'su contraseña tiene {nmen5} numeros menor de 5 y {nmi5} numeros mayor o igual que 5, con un total de {n} numeros')
    
print('Tiene un total de ',cc,'contraseñas correctas')

