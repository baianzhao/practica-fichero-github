prod=input().split('-')
nombre=[]
precio=[]
stock=[]
for x in prod:
    d=x.split(':')
    nombre.append(d[0])
    precio.append(float(d[1]))
    stock.append(int(d[2]))
print(nombre, precio, stock)
total=0
for y in range(len(precio)):
    y=int(y)
    total+=(precio[y]) * (stock[y])
print('el total de dinero es de: ',total)
mascaro=0
cosacara=''
for i in range(len(precio)):
    if precio[i] > mascaro:
        mascaro=precio[i]
        cosacara=nombre[i]
print('el producto mas caro es: ', cosacara)
 
stock0=[]
for x in range(len(stock)):
    if stock[x]==0:
        stock0.append(nombre[x])
print('los productos con stock 0 son o es: ',stock0)

for z in range(len(stock) - 1, -1, -1):
    if stock[z]==0:
        nombre.pop(z)
        stock.pop(z)
        precio.pop(z)
print(nombre, precio, stock)
