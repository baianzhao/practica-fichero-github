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
    merror=f'/Error, el password té una longitud de {password_lenth} caràcters i no compleix els requisits'
    print(merror)
    