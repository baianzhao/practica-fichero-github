#80. Utilizando listas, crea un programa que te permita determinar si un número es decimal o no. 

d=input('introduce un numero decimal')
dd=d.split('-')
print(dd)
e=0
c=0
for x in dd:
    if x.isnumeric()!=True:
        e+=1
    if x.isalpha()==True:
        e+=1
    if x=='.':
        c+=1
   

if dd[::-1]=='.':
    e+=1



if e>=1 or c<1:
    print('error')
else:

    print('el valor es decimal')





