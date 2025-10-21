#mostrar por pantalla todas las instrucciones
print('INSTRUCCIONS')
print('1. La longitud del password té que tenir entre 6 i 8 caràcters')
print('2.forçar els seguents valors segons la posició indicada:')
print('     Posició 1 Un número major o igual a 1 i menor o igual que 5.')
print('     Posició 2 Una lletra minúscula.')
print('     Posició 3 Una lletra majúscula.')
print('     Posició 4 Un dels següent símbols *, _, @')
print('     Posició 5 Una lletra minúscula')
print('     Posició 6 Un número major o igual 6 i menor o igual que 9')
print('     Posició 7 Un dels seguent símbols &, /, #')
print('     Posició 8 Un número menor o igual que 5')
#asignar el valor de la contraseña
password=input('Introduce una palabra clave')
num_err=0
merror=''
#detectar el numero de letras
password_lenth=len(password)
if password_lenth >= 6 and password_lenth <= 8:
    num_err=num_err
    merror=merror
else:
    num_err=num_err+1
    merror=merror+f'/Error, el password té una longitud de {password_lenth} caràcters i no compleix els requisits'
    print(merror)
#comprovar caracter 1
n1=int(password[0])
if n1 > 5 or n1 < 1:
    num_err=num_err+1
    merror=merror+f'/Error, en el caracter 1'
else:
    num_err=num_err
    merror=merror
#comprovar caracter 2
n2=password[1]
if n2.islower() == False:
    num_err=num_err +1
    merror=merror+f'/Error, en el caracter 2'
else:
    num_err=num_err
    merror=merror

#comprovar caracter 3
n3=password[2]
if n3.isupper() == False:
    num_err=num_err +1
    merror=merror+f'/Error, en el caracter 3'
else:
    num_err=num_err
    merror=merror
#comprovar caracter 4
if password[3] == '*' or password[3] == '_' or password[3] == '@':
    num_err=num_err
    merror=merror
else:
    num_err=num_err +1
    merror=merror+f'/Error, en el caracter 4'
#comprovar caracter 5
n4=password[1]
if n4.islower() == False:
    num_err=num_err +1
    merror=merror+f'/Error, en el caracter 5'
else:
    num_err=num_err
    merror=merror
#comprovar caracter 6
if password_lenth != 6:
    num_err=num_err
else:
    n6=int(password[5])
if n6 > 9 or n6 < 6:
    num_err=num_err+1
    merror=merror+f'/Error, en el caracter 6'
#comprovar caracter 7
if password_lenth==6:
    num_err=num_err
    merror=merror
elif password_lenth == 7:
    if password[6] == '&' or password[6] == '/' or password[6] == '#':
        num_err=num_err
        merror=merror
    else:
        num_err=num_err +1
        merror=merror+f'/Error, en el caracter 7'

elif password_lenth == 8:
    if password[6] == '&' or password[6] == '/' or password[6] == '#':
        num_err=num_err
        merror=merror
    else:
        num_err=num_err +1
        merror=merror+f'/Error, en el caracter 7'
#comprovar caracter8
if password_lenth==6:
    num_err=num_err
    merror=merror
elif password_lenth==7:
    num_err=num_err
    merror=merror
elif password_lenth == 8:
    if password[7] <= 5:
        num_err=num_err
        merror=merror
    else:
        num_err=num_err +1
        merror=merror+f'/Error, en el caracter 8'

#mostrar el resultado
print('el numero total de errores es: ', num_err)
print(merror)

