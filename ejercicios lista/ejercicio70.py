#70. Crea un programa que permita introducir x palabras en una lista llamada lista1. Una vez 
#introducidas, crea una nueva lista, llamada lista2, exactamente igual a lista1. Se deben mostrar por 
#pantalla el contenidos de lista1 en orden ascendente y lista2 en orden descendente. Respeta el 
#formato de entrada y salida tal y como se muestra en el testeo.

cn=int(input('introduce la cantidad de palabras que quiere introducir'))
l=[]
for m in range(cn):
    a=str(input('introduce palabra'))
    l.append(a)

print(l)
l2=l[::-1]
print(l2)