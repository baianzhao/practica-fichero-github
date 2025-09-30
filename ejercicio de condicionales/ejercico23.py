#Modifica el programa anterior para establecer si la nota es un excelente (8.5 a 10), un notable (>=6.5 -<8.5), satisfactorio (<6.5 -5) o insuficiente (<5). Controla que la nota introducida esté entre 0 y 10. Utilizar elif sin operadores lógicos.
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