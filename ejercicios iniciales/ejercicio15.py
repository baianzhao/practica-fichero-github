#Utiliza el valor Pi de la librería math para calcular el área y volumen de un cilindro,introduciendo por teclado el valor de radio y altura. Resultado con 2 decimales.

h=float(input('introduce la altura'))
r=float(input('introduce el radio'))
import math
areabase=(math.pi)*2*r**2
arealado=2*(math.pi)*r*h
areatotal=areabase+arealado
volumen=(math.pi)*h*r**2
areatotal=round(areatotal, 2)
volumen=round(volumen, 2)
print('el area del cilindro es: ',areatotal)
print('el volumen del cilindro es: ',volumen)
