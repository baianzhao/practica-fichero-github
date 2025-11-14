#A partir del programa anterior, modifica el código para que sea el usuario quién introduzca el 
#número de veces que desea que repita la frase Buenos días. Con While

n=int(input('introduce el numero de veces que quiere que se repita el bucle'))
while n>0:
    print('Buenos días')
    n-=1
