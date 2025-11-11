#Realiza un programa donde el usuario introduzca por teclado 2 intervalos, por pantalla se debe 
#mostrar el rango de números teniendo en cuenta que se a<b la secuencia será incremental y si a>b 
#la secuencia en descenso. Respeta el formato de salida

i1=int(input('introduce el primer intervalo'))
i2=int(input('introduce el segundo intervalo'))

if i1<i2:
    for n in range(i1, (i2+1), 1):
        print(n, end='-')
    
elif i2<i1:
    for n in range(i1, (i2-1), -1):
        print(n, end='-')
    
