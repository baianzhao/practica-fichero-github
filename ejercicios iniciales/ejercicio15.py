#Utiliza el valor Pi de la librería math para calcular el área y volumen de un cilindro, introduciendo por teclado el valor de radio y altura. Resultado con 2 decimales.
import math
h=int(input('introduce altura'))
r=int(input('introduce el radio'))
ab=(math.pi)*2*r**2
ac=2*(math.pi)*r*h
areabase=round(ab, 2)
arealado=round(ac, 2)
totalarea=areabase*arealado

print('')