#73. Diseña un programa que compruebe si los valores de la lista1 (casa,mesa,sal,sol,agua) están 
#repetidos o no en la lista2 (casa,luz,tres,tren,sol,pan). Haz que permita visualizar que palabras se 
#repiten y cuales no

l1=['casa','mesa','sal','sol','agua']
l2=['casa','luz','tres','tren','sol','pan']
l3=[]
l4=[]
for x in l1:
    for y in l2:
        if x in l1 and y in l2 and x==y:
            l3.append(x)


l4=l1+l2
l5=set(l4)
l6=[]
for n in l2:
    if n not in l3:
        l6.append(n)



print(l4)
print(l5)

print(f'los repetidos son {l3}')

print(f'los no repetidos son{l6}')
