# Programa que pregunte cuantas notas quiero introducir y para cada nota diga si estoy aprobado o suspendido.
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
            if x>=5:
                print('asignatura aprovada')
            else:
                print('asignatura suspendida')

