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
#detectar el numero de letras
password_lenth=len(password)
if password_lenth >= 6 and password_lenth <= 8:
    if password_lenth == 6:
        p1=password[0]
        p2=password[1]
        p3=password[2]
        p4=password[3]
        p5=password[4]
        p6=password[5]
        if p1 != 1 and p1 != 5 and p1 > 5:
            print('Error en el caràcter 1')
            num_err=num_err +1
        else:
            uplow=p2.isupper
            if uplow == False:
                print('Error en el caràcter 2')
                num_err= num_err +1
            else:
                print()
        


    elif password_lenth == 7:
        print('9')
    
    elif password_lenth == 8:
        print('f')

else:
    print('Error, el password té una longitud de ',password_lenth,' caràcters i no compleix els requisits')#mensaje de error

    

