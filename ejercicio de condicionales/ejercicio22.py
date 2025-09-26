#. Programa que al introducir una nota por teclado te diga si has aprobado o suspendido. Si la nota es menos de un 5 es suspenso y si la nota es 5 o mayor estás aprobado.
nota=float(input('introduce tu nota'))
if nota >=0 and nota <= 10:
    if nota >= 5:
        print('has sacado un: ',nota,' has aprovado')
    else:
        print('has sacado un: ',nota,' has suspendido')
else:
    print('tu nota no esta dentro del rango')