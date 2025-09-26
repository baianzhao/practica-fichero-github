#Programa que introduzca dos números y devuelva cuál de los dos es mayor, menor o son iguales
num1=int(input('introduzca un numero'))
num2=int(input('introduzca otro numero'))
if num1 > num2:
    print('el numero ',num1,'es mayor que ',num2)
elif num1 < num2:
    print('el numero ',num2,'es mayor que ',num1)
else:
    print('los dos numeros son iguales')