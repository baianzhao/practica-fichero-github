#63. Realiza un programa que permita tirar 100 veces un dado y nos presente por pantalla el número
#de veces que se repite cada número.
n0=0
n1=0
n2=0
n3=0
n4=0
n5=0
n=0
import random
for a in range(1000000000000000000000000000000000000000000000000000):
    
    i=random.randint(0, 5)
    if i==0:
        n0+=1
    elif i==1:
        n1+=1
    elif i==2:
        n2+=1
    elif i==3:
        n3+=1
    elif i==4:
        n4+=1
    elif i==5:
        n5+=1
    n+=1

print(f'numero de veces el 0 repetido:{n0}')
print(f'numero de veces el 1 repetido:{n1}')
print(f'numero de veces el 2 repetido:{n2}')
print(f'numero de veces el 3 repetido:{n3}')
print(f'numero de veces el 4 repetido:{n4}')
print(f'numero de veces el 5 repetido:{n5}')
