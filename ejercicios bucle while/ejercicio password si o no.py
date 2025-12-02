print('Las 3 contraseñas deben de tener como minimo 3 numeros, 3 letras y 2 simbolos cada una')#mostrar las condiciones
ci=0
cc=0#total de contraseñas correctas
sn=False

while sn==False:

    for password in range(3):#bucle para repetir 3 veces la introduccion de contraseñas
        
        n=0#variable para total de numeros
        l=0#variable para total de letras
        s=0#variable para total de simbolos
        lm=0#variable para letras mayusculas
        lmi=0#variable para letras minusculas
        nmi5=0#variables para numeros mayor o igual que 5---esto es parte de 'distinguir rangos', es decir, detecta 2 'tipos' de numeros
        nmen5=0#variables para numeros menor de 5
        psw=input('introduce una contraseña')#pedir contraseña
        for caracter in psw:
            if caracter.isalpha()==True:#si es una letra
                l+=1#letras +1
                if caracter.islower()==True:#detectar si es mayuscula o minuscula
                    lmi+=1
                else:
                    lm+=1
            elif caracter in '1234567890':#detectar si el caracter es un digito
                n+=1
                if int(caracter)<5:#detectar si el numero es menor que 5.
                    nmen5+=1
                else:
                    nmi5+=1

            else:#si no son ni letras ni numeros, son simbolos
                s+=1
        if n<3 or l<3 or s<2:#si hay mas de 3 letras, mas de 3 numeros y mas de 2 simbolos, es correcta la contraseña
            print('Error, la contraseña no cumple con los requisitos')
            ci+=1
        else:
            print('la contraseña es correcta')
            cc+=1
        print(f'su contraseña tiene un total de {lm} letras mayusculas y {lmi} letras minusculas, un total de {l} letras')
        print(f'su contraseña tiene {nmen5} numeros menor de 5 y {nmi5} numeros mayor o igual que 5, con un total de {n} numeros')
        
    print('Tiene un total de ',cc,'contraseñas correctas')#despues de repetir 3 veces, se muestra el numero total de contraseñas correctas
    print('Tiene un total de ',ci,'contraseñas incorrectas')#mostrar el numero de contraseñas incorrectas.
    yn=input('desea continuar? si/no')
    if yn=='si':
        sn=False
    elif yn=='no':
        sn=True
    else:
        print('error, fin del programa')
