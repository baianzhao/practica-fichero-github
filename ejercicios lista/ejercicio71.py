#71. Haz un programa que permita al usuario introducir letras en una lista (cantidad indefinida), en 
#esta lista no deben almacenarse las letras que se han introducido repetidas.
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
    l3.append(r)

print(l3)