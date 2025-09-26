#Calcula el índice de masa corporal IMC de una persona, introduciendo por teclado el peso (en kg) y dividiendo por la estatura (en metros y elevado al cuadrado). Si el resultado es igual o superior a 25, debe aparecer un mensaje informando de sobrepeso.
weight=float(input('introduzca su peso(en kg)'))
high=float(input('introduzca su altura(en m)'))
imc=weight/high**2
imc=round(imc, 2)
if imc >= 25:
    print('si pesas ,',weight,'kilos y mides ',high,', tu IMC es de ',imc,'HAY SOBREPESO!!')
else:
    print('si pesas ',weight,'kilos y mides ',high,', tu IMC es de ',imc)

