#63. Realiza un programa que permita tirar 100 veces un dado y nos presente por pantalla el número
#de veces que se repite cada número.
n6=0
n1=0
n2=0
n3=0
n4=0
n5=0
n=0
import random
for a in range(100):
    
    i=random.randint(1, 6)
    if i==6:
        n6+=1
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

print(f'numero de veces el 1 repetido:{n1}')
print(f'numero de veces el 2 repetido:{n2}')
print(f'numero de veces el 3 repetido:{n3}')
print(f'numero de veces el 4 repetido:{n4}')
print(f'numero de veces el 5 repetido:{n5}')
print(f'numero de veces el 6 repetido:{n6}')