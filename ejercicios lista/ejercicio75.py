#75. Crea una lista con el siguiente nombre lista1 y su contenido: a,b,D,x,r,X,3,h,w,2,i. Presenta por
#pantalla los siguientes resultados:
#a. Cantidad total de valores
#b. Cantidad de números
#c. Cantidad de letras
#d. Cantidad de mayúsculas
#e. Suma de los valores numéricos

lista1=['a','b','D','x','r','X','3','h','w','2','i']

a=0
b=0
c=0
d=0
e=0


for x in lista1:
    if x in '1234567890':
        b+=1
        x=int(x)
        e+=x
        x=str(x)
    if x.isalpha()==True:
        c+=1
        if x.isupper()==True:
            d+=1
    a+=1
    
print('Número de valores:',a)
print('Cantidad de números:',b)
print('Cantidad de letras:',c)
print('Cantidad de mayúsculas:',d)
print('Suma total de números:',e)
