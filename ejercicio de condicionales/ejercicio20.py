#A partir del ejercicio anterior, forzar que el usuario solo pueda introducir por teclados números entre 0 y 10.
num1=int(input('introduzca un numero'))
num2=int(input('introduzca otro numero'))
if num1 >= 0 and num1 <= 10 and num2 >= 0 and num2 <= 10:
    if num1 > num2:
        print('el numero ',num1,'es mayor que ',num2)
        
    elif num1 < num2:
        print('el numero ',num2,'es mayor que ',num1)
        
    else:
        print('los dos numeros son iguales')

else:
    print('uno de los numeros esta fuera del rango')