#Programa que calcula una ecuación de segundo grado. Controla que el valor de la raíz cuadrada no de un valor negativo.
import math
a=int(input('introduce la a de una equacion de 2 grado'))
b=int(input('introduce la b de una equacion de 2 grado'))
c=int(input('introduce la c de una equacion de 2 grado'))
if b**2-4*a*c >=0:
    x1=-b+math.sqrt(b**2-4*a*c)
    x1=x1/2*a
    x2=-b-math.sqrt(b**2-4*a*c)
    x2=x2/2*a
    print('el valor de x1 es ',x1)
    print('el valor de x2 es ',x2)
else:
    print('el valor de la raiz quadrada es negativa, no se puede calcular')
