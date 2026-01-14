#74. A partir del programa anterior, haz que se visualicen tanto las palabras que se repiten o no de
#entre las 2 listas.

l1=['casa','mesa','sal','sol','agua']
l2=['casa','luz','tres','tren','sol','pan']
l3=[]
l4=[]

for x in l1:
    for y in l2:
        if x in l1 and y in l2 and x==y:
            l3.append(x)
total=l1+l2
for n in total:
    if n not in l3:
        l4.append(n)



print(f'los repetidos son {l3}')

print(f'los no repetidos son{l4}')
