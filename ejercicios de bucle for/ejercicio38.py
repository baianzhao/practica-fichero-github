#A partir del programa anterior, establece los rangos para que el usuario no pueda introducir notas inferiores a 0 y superiores a 10
nn=input('introduce el numero de notas que quiere introducir')
if nn.isalpha()==True:
    print('error')
else:
    nn=float(nn)
    if nn % 1 != 0:
        print('error')
    else:
        nn=int(nn)
        for n in range(nn):
            x=float(input('introduce la nota'))
            if x>10 or x<0:
                print('error')
            else:
                if x>=5:
                    print('asignatura aprovada')
                else:
                    print('asignatura suspendida')