#Programa que sume los n primeros números naturales. n Lo introduce el usuario.
n=int(input('introduce en numero de numeros naturales que quiere sumar'))
x=0
y=1
for num in range(n):
    x=x+y
    y+=1
print(x)

