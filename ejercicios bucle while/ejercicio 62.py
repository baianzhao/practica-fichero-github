#Realiza un programa que pida dos números por teclado y presente por pantalla qué números 
#hay pares e impares en ese rango. Utiliza for. Contempla si primer valor es superior al segundo

n1=int(input('introduce el primer numero'))
n2=int(input('introduce el segundo numero'))
nn1=0
nn2=0
#pares
if n1<n2:
    print('los numeros pares son:', end='')
    if n1%2==0:

        for n in range(n1,n2,2):
            if n==n2 or n==n2-2 or n==n2-1:
                print(n, end='')
            else:
                print(n, end='-')

    else:
        for n in range(n1+1,n2,2):
            if n==n2 or n==n2-2 or n==n2-1:
                print(n, end='')
            else:
                print(n, end='-')

elif n2<n1:
    print('los numeros pares son:',end='')
    if n1%2==0:
        for n in range(n2,n1,2):
            if n==n1 or n==n1-2 or n==n1-1:
                print(n, end='')
            else:
                print(n, end='-')
    else:
        for n in range(n2,n1,1):
            if n==n1 or n==n1-2 or n==n1-1:
                print(n, end='')
            else:
                print(n, end='-')

    