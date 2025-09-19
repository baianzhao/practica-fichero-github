#Realiza un programa que, introduciendo en los valores de lado, base menor, base mayor y altura de un trapecio isósceles, nos devuelva por pantalla en el área y el perímetro
lado=float(input('introduzca el valor de un lado de un trapezio isosceles'))
b=float(input('introduzca el valor de la base menor de un trapezio isosceles'))
bb=float(input('introduzca el valor de la base mayor de un trapezio isosceles'))
h=float(input('introduzca el valor de la altura de un trapezio isosceles'))
perimetro=lado*2+b+bb
area=(bb+b)*h
area=area/2
print('el perimetro del trapezio es: ', perimetro)
print('el area del trapezio es: ',area)
