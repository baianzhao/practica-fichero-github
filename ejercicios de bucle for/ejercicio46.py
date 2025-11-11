#A partir del programa anterior, soluciona el error que se produce en el test anterior con la palabra Abrigo utilizando únicamente una instrucción.

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