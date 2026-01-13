frs=input('introduce valores separados por guion')

l=frs.split('-')
ln=[]
ll=[]
print(l)

l12=set(l)
l2=[]
for r in l12:
    l2.append(r)

    
for n in l2:
    if n.isnumeric()==True:
        ln.append(n)
    elif n.isalpha()==True:
        ll.append(n)

    
nt=0
for m in ln:
    m=int(m)
    nt+=m

print(ll)
print(ln)
print(f'la suma de todos los numeros es de {nt}')