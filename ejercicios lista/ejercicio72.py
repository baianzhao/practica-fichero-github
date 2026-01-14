#72. A partir del ejercicio anterior, se da por hecho que las vocales con o sin acento son repetidas y 
#no deben almacenarse en la lista

l=[]
t=False
while t==False:
    ap=str(input('introduce una letra'))
    l.append(ap)
    ask=input('desea continuar?? si/no')
    if ask=='no':
        t=True
        break

l2=set(l)
l3=[]
for r in l2:
    if r in 'àá':
        r='a'
        l3.append(r)
    
    if r in 'éè':
        r='e'
        l3.append(r)

    if r in 'íì':
        r='i'
        l3.append(r)

    if r in 'óò':
        r='o'
        l3.append(r)

    if r in 'úù':
        r='u'
        l3.append(r)


print(l3)