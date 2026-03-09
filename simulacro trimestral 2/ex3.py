prod=input().split('-')
print(prod)
nom=[]
prec=[]
stock=[]
resumen_max_product=''
res_max=''
for x in prod:
    d=x.split(':')
    nom.append(d[0])
    prec.append(float(d[1]))
    stock.append(int(d[2]))
total=0
for i in range(len(prec)):
    total+=prec[i]*stock[i]

maxim=prec[0]
ind=0
for z in range(0,len(prec)):
    if prec[z]>maxim:
        maxim=prec[z]
        ind=z
res_max=nom[z]
for x in range(len(stock)):
    if stock[x]==0:
        resumen_max_product=nom[x]


for i in range(len(stock) - 1, -1, -1):
    if stock[i] == 0:    
        nom.pop(i)  
        prec.pop(i)     
        stock.pop(i)


print(resumen_max_product)
print(res_max)
print(nom)
print(prec)
print(stock)
print(total)
