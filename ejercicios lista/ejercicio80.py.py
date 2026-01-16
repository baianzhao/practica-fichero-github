#80. Utilizando listas, crea un programa que te permita determinar si un número es decimal o no. 

d=input('introduce un numero decimal')
dd=d.split('.')
nd,c,e=0,0,0
for x in dd:
    x=str(x)
    if x.isnumeric()==True:
        x=x
    
    else:
        e+=1

if len(dd)==2 and e==0 and dd[::-1]!='.':
    print('correcto')
else:
    print('error')




