#Realiza un programa que pida dos números por teclado y presente por pantalla qué números 
#hay pares e impares en ese rango. Utiliza for. Contempla si primer valor es superior al segundo

n1=int(input('introduce el primer numero'))
n2=int(input('introduce el segundo numero'))
nnp=''
nni=''

if n1<n2:
    for i in range(n1, n2):
        if i%2==0:
            nnp+=str(i)
            nnp+='-'
        elif i%2!=0:
            nni+=str(i)
            nni+='-'
            
elif n1>n2:
    for i in range(n2, n1):
        if i%2==0:
            nnp+=str(i)
            nnp+='-'
        elif i%2!=0:
            nni+=str(i)
            nni+='-'

print(f'los numeros pares son:{nnp[:-1]}')
print(f'los numeros impares son:{nni[:-1]}')