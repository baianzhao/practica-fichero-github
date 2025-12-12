print('Las 3 contraseñas deben de tener como minimo 3 numeros, 3 letras y 2 simbolos cada una')#mostrar las condiciones
ci=0
cc=0#total de contraseñas correctas
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

#-------------------------------------------------------------------------------------------------------------------
#Realiza la VERSIÓN 2 de la actividad Password utilizando bucles (for).  

#Aspectos a tener en cuenta en el desarrollo de la actividad:  

#1. Realiza las modificaciones correspondientes en una copia del fichero versión 1.  

#2. En esta versión, no debes contemplar que se cumplan las condiciones en las posiciones de los índices, pero sí que el total de criterios se cumplan: 3 números (distinguiendo rangos), 3 letras (distinguiendo mayúsculas o minúsculas), 2 símbolos, etc.  

#3. Tiene que existir un bucle que recorra el password y realice las comprobaciones y los contajes necesario.  

#4. El usuario debe poder introducir un total de 3 passwords en una misma ejecución del programa. Además de visualizar por pantalla si el password cumple o no con los criterios, debe aparecer por pantalla el número de passwords que ha introducido con formato correcto e incorrecto. 

#5. Crea un testeo de 10 pruebas que permita la evaluación del código, puedes compartir testeos con otros compañeros. Añádelos como comentario en tu código.  

#6. Tienes libertad para establecer otros criterios que consideres oportunos en el programa. Explícalos con claridad a través de comentarios en el código  

#7. La entrega la debes realizar por Managebac utilizando la misma publicación del Password versión 1 
#-------------------------------------------------------------------------------------------------------------------
#testeo:

#1
# ABc128&! , 555hO/· , H$De15&4 
#la contraseña es correcta 
#su contraseña tiene un total de 2 letras mayusculas y 1 letras minusculas, un total de 3 letras 
#su contraseña tiene 2 numeros menor de 5 y 1 numeros mayor o igual que 5, con un total de 3 numeros 
#Error, la contraseña no cumple con los requisitos 
#su contraseña tiene un total de 1 letras mayusculas y 1 letras minusculas, un total de 2 letras 
#su contraseña tiene 0 numeros menor de 5 y 3 numeros mayor o igual que 5, con un total de 3 numeros 
#la contraseña es correcta 
#su contraseña tiene un total de 2 letras mayusculas y 1 letras minusculas, un total de 3 letras 
#su contraseña tiene 2 numeros menor de 5 y 1 numeros mayor o igual que 5, con un total de 3 numeros 
#Tiene un total de  2 contraseñas correctas 
#-------------------------------------------------------------------------------------------------------------------

#2
#1357acE&&· , CCy$$!0245 , 9r%FC1@2 
#la contraseña es correcta 
#su contraseña tiene un total de 1 letras mayusculas y 2 letras minusculas, un total de 3 letras 
#su contraseña tiene 2 numeros menor de 5 y 2 numeros mayor o igual que 5, con un total de 4 numeros 
#la contraseña es correcta 
#su contraseña tiene un total de 2 letras mayusculas y 1 letras minusculas, un total de 3 letras 
#su contraseña tiene 3 numeros menor de 5 y 1 numeros mayor o igual que 5, con un total de 4 numeros 
#la contraseña es correcta 
#su contraseña tiene un total de 2 letras mayusculas y 1 letras minusculas, un total de 3 letras 
#su contraseña tiene 2 numeros menor de 5 y 1 numeros mayor o igual que 5, con un total de 3 numeros 
#Tiene un total de  3 contraseñas correctas 
#-------------------------------------------------------------------------------------------------------------------

#3
# 1234abcd , zzzzzzzzzz , Hola$$33 
#Error, la contraseña no cumple con los requisitos 
#su contraseña tiene un total de 0 letras mayusculas y 4 letras minusculas, un total de 4 letras 
#su contraseña tiene 4 numeros menor de 5 y 0 numeros mayor o igual que 5, con un total de 4 numeros 
#Error, la contraseña no cumple con los requisitos 
#su contraseña tiene un total de 0 letras mayusculas y 10 letras minusculas, un total de 10 letras 
#su contraseña tiene 0 numeros menor de 5 y 0 numeros mayor o igual que 5, con un total de 0 numeros 
#Error, la contraseña no cumple con los requisitos 
#su contraseña tiene un total de 1 letras mayusculas y 3 letras minusculas, un total de 4 letras 
#su contraseña tiene 2 numeros menor de 5 y 0 numeros mayor o igual que 5, con un total de 2 numeros 
#Tiene un total de  0 contraseñas correctas 
#-------------------------------------------------------------------------------------------------------------------

#4
# JH5%!p571 , GG66)(6bc , 123qT& 
#la contraseña es correcta 
#su contraseña tiene un total de 2 letras mayusculas y 1 letras minusculas, un total de 3 letras 
#su contraseña tiene 1 numeros menor de 5 y 3 numeros mayor o igual que 5, con un total de 4 numeros 
#la contraseña es correcta 
#su contraseña tiene un total de 2 letras mayusculas y 2 letras minusculas, un total de 4 letras 
#su contraseña tiene 0 numeros menor de 5 y 3 numeros mayor o igual que 5, con un total de 3 numeros 
#Error, la contraseña no cumple con los requisitos 
#su contraseña tiene un total de 1 letras mayusculas y 1 letras minusculas, un total de 2 letras 
#su contraseña tiene 3 numeros menor de 5 y 0 numeros mayor o igual que 5, con un total de 3 numeros 
#Tiene un total de  2 contraseñas correctas 














