#Repite el programa número 23 pero en esta ocasión utilizando operadores lógicos.
nota=float(input('introduce tu nota'))
if nota >= 0 and nota <= 10:
    if nota >= 8.5:
        print('tu nota es: ',nota,' has sacado un excelente')
    elif nota < 8.5 and nota >= 6.5:
        print('tu nota es: ',nota,' has sacado un notable')
    elif nota < 6.5 and nota >= 5:
        print('tu nota es: ',nota,' has sacado un suficiente')
    else:
        print('tu nota es: ',nota,' has suspendido')

else:
    print('tu nota introducida no esta dentro del rango')