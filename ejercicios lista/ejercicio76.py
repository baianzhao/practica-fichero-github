#76. A partir de la lista del enunciado anterior, haz que el programa visualice por un lado las letras
#y por otro los números permitiendo escoger orden ascendente o descendente. Como observarás
#en la salida, el orden de las letras no es correcto, busca la manera de solucionarlo.

lista1=['a','b','D','x','r','X','3','h','w','2','i']
aod=int(input('Introduce 1 para visualizar en orden ascendente o 2 descendente:'))
#n
n=[]
nint=[]


#l
l=[]
llower=[]
lsorted=[]
#detectar numero o letra
for x in lista1:
    if x in '1234567890':
        n.append(x)
    if x.isalpha()==True:
        l.append(x)
#procesar listas  
for m in n:
    mm=int(m)
    nint.append(mm)

for y in l:
    yy=y.lower()
    llower.append(yy)


#ver 1 o 2


if aod==1:
    nsorted=sorted(nint)
    print(nsorted)
    llower.sort()
    print(llower)

elif aod==2:
    nsorted=sorted(nint, reverse=True)
    print(nsorted)
    llower.sort(reverse=True)
    print(llower)


