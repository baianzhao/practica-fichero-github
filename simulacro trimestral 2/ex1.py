inp=input().split(',')
lista=[]
for x in inp:
    x=int(x)
    lista.append(x)
lista.sort()
print(lista)
lista.pop(0)
lista.pop(len(lista)-1)
print(lista)
suma=sum(lista)
media=suma/len(lista)
media_formateada=float(media)
print(f'{media:.2f}')
if media_formateada<5:
    print('rendimiento bajo')
elif media_formateada>=5 and media_formateada<=10:
    print('rendimiento medio')
elif media_formateada>10:
    print('rendimiento alto')
