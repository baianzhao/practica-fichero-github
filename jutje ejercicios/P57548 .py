n=input()
n2=n.split()
if len(n2)!=2:
    i=input()
    n2.append(i)
    suma=0
    for x in n2:
        x=int(x)
        suma+=x
    print(suma)
else:
    suma=0
    for x in n2:
        x=int(x)
        suma+=x
    print(suma)
