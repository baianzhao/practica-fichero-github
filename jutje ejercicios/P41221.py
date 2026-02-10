n=input()
n2=n.split()
while len(n2)!=3:
    i=input()
    if i=='':
        i=i
    else:
        n2.append(i)

    if len(n2)==3:
        break
suma=0
for x in n2:
    x=int(x)
    suma+=x
print(suma)
