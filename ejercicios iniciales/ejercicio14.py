# Realiza un programa que a partir de introducir el diámetro de un círculo calcule el área y perímetro.Imprta la lbrería match y utiliza el valor PI para hacer el cálculo. Redondea el resultado a un decimal.
diametre=float(input('introduzca un diametro de un circulo'))
radio=diametre/2

import math
pinumero=(math.pi)
area=pinumero*radio**2

perimetro=diametre*(math.pi)

area=round(area, 1)
perimetro=round(perimetro, 1)

print('el valor del area del circulo es: ',area)
print('el valor del perimetro es: ',perimetro)

