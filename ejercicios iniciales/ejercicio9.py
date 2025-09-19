# programa que pida los segundos y muestre por pantalla y en la misma frase los minutos y las horas
seg=int(input('introduzca un numero de segundos'))
min=seg/60
hor=min/60
hor=round(hor, 2)
print('el numero en minutos es: ',min,'el numero en horas es: ',hor)