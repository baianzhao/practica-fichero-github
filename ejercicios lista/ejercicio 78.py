#78. A partir de la lista definida en el ejercicio 75, haz que el programa pregunte qué valor se desea
#eliminar de la lista, siendo únicamente los números los valores permitidos para suprimir

lista1=['a','b','D','x','r','X','3','h','w','2','i']

si='si'
while si=='si':
    v=input('introduce el valor que quiere borrar')
    if v in lista1:
            lista1.remove(v)

    elif v not in lista1:
          print('el valor no esta en la lista')

    si=input('desea continuar? si/no')

    if si!='si':
          si='no'
          
    elif si=='si':
          si=si

    print(lista1)
