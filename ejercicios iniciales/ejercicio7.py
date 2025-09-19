#programa que calcule dos operandos con los 7 operadores vistos en clase. ¿Cómo puedes forzar que el resultado de la división tenga 2 decimales?
num1=int(input('introduce un numero entero'))
num2=int(input('introduce otro numero'))
suma=num1+num2
resta=num1-num2
multi=num1*num2
divi=num1/num2
divi=round(divi, 2)
pot=num1**num2
import math
raiz1=math.sqrt(num1)
raiz2=math.sqrt(num2)
diventera=num1//num2
print('la suma del numero 1 y 2 es de: ',suma)
print('la resta del numero 1 y 2 es de: ',resta)
print('el resultat del num1 multiplicat per el num2 es: ',multi)
print('la divisio del num1 dividit el num2 es de: ',divi)
print('la potencia del num1 elevado al num2 es de: ',pot)
print('la arrel quadrada del num 1 es de: ',raiz1)
print('la arrel quadrada del num 2 es de: ',raiz2)
print('la divisio entera del numero 1 entre el 2 es de: ',diventera)
