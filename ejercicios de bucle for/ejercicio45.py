#Realiza un programa que permita introducir una palabra por teclado y puedas recorrer el string distinguiendo vocales y las consonantes:

palabra=input('introduce una palabra')
palabra=palabra.lower()
c=''
v=''
for x in palabra:
    if x in 'aeiouàáèéíìòóúù':
        v=v+x
    else:
        c=c+x

print('Las vocales de la palabra ',palabra,'son:',v, end='')
print()
print('Las consonanates de la palabra ',palabra,'son:',c, end='')