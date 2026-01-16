#76. A partir de la lista del enunciado anterior, haz que el programa visualice por un lado las letras
#y por otro los números permitiendo escoger orden ascendente o descendente. Como observarás
#en la salida, el orden de las letras no es correcto, busca la manera de solucionarlo.

lista1=['a','b','D','x','r','X','3','h','w','2','i']
aod=int(input('Introduce 1 para visualizar en orden ascendente o 2 descendente:'))
n=[]
l=[]

for x in lista1:
    if x in '1234567890':
        n.append(x)
    if x.isalpha()==True:
        l.append(x)

n=list(map(int, n))


if aod==1:
    n=sorted(n)
    l.sort(key=lambda v: v.lower(),reverse=False)
elif aod==2:
    n=sorted(n, reverse=True)
    l.sort(key=lambda v: v.lower(),reverse=True)
    
print(n)
print(l)
    
    
    
    
    
    
    
    
    
    
    
    

   


