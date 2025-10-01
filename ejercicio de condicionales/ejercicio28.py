# Mejora el programa anterior para controlar también la introducción de símbolos. Utiliza elif
let=input('introduce algo')
mayus=let.isupper()
digit=let.isnumeric()
sidigit=let.isdigit()
if mayus == True and digit == False:
    print('la letra es mayuscula')

elif digit == True and sidigit == True:
    print('es un numero')
elif mayus == False and digit == False and sidigit==False:
    if digit== False and mayus!= False and mayus!= True:
        print('es minuscula')
    else:
        print('es un simbolo')