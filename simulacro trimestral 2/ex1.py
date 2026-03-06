puntos=input().split(',')
lista_media=[]
for x in puntos:
    x=int(x)
    lista_media.append(x)
lista_media.sort()
lista_media.pop(0)
lista_media.pop(len(lista_media)-1)
print(puntos)
print(lista_media)
suma=sum(lista_media)
media=suma/len(lista_media)
media=round(media)
media2=f'{media:.2f}'
print(media2)
if media<5:
    print('rendimiento bajo')
elif media<=10 and media >=5:
    print('rendimiento medio')
elif media>10:
    print('rendimiento alto')


