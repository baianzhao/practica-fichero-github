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
if password_lenth < 6 or password_lenth > 8:
    num_err=1
    print(f'Error, el password té una longitud de {password_lenth} caràcters i no compleix els requisits')
else:
    n1=password[0]
    n2=password[1]
    n3=password[2]
    n4=password[3]
    n5=password[4]
    n6=password[5]
    
    if password_lenth==7:
        n7=password[6]
    elif password_lenth==8:
        n7=password[6]
        n8=password[7]
#n1

    if n1.isalpha()== True:
        num_err=num_err+1
        merror=merror+'/Error en el carácter 1/'
    else:
        if int(n1)>8 or int(n1)<6:
            num_err=num_err+1
            merror=merror+'/Error en el carácter 1/'

#n2
    if n2.isalpha()==False:
        num_err=num_err +1
        merror=merror+'/Erroren el caracter 2/'

    else:
        if n2.islower() == False:
            num_err=num_err +1
            merror=merror+'/Erroren el caracter 2/'

#n3
    if n3.isalpha()== False:
        num_err=num_err +1
        merror=merror+f'/Error en el caracter 3/'
    else:
        if n3.isupper() == False:
            num_err=num_err +1
            merror=merror+'/Error en el caracter 3/'
    
#n4
    s41=n4.find('*' or '_' or '@')
    if s41 >0:
       num_err=num_err +1
       merror=merror+'/Error en el caracter 4/' 
    

            

#n5
    if n5.isalpha()==False:
        num_err=num_err +1
        merror=merror+'/Erroren el caracter 5/'

    else:
        if n5.islower() == False:
            num_err=num_err +1
            merror=merror+'/Erroren el caracter 5/'

#n6
    if n6.isnumeric()== False:
        num_err=num_err +1
        merror=merror+'/Erroren el caracter 6/'
    else:
        if int(n6) >9 or int(n6)< 6:
            num_err=num_err +1
            merror=merror+'/Erroren el caracter 6/'
#n7

    if password_lenth==7 or password_lenth==8:
        s71=n7.find('&' or '/' or '#')
    if s71 >0:
       num_err=num_err +1
       merror=merror+'/Error en el caracter 7/' 

#n8
    if password_lenth==8:
        if n8.isnumeric()==False:
            num_err=num_err +1
            merror=merror+'/Erroren el caracter 8/'
        else:
            if int(n8) > 5:
                num_err=num_err +1
                merror=merror+'/Erroren el caracter 8/'

print('el numero total de errores es de: ',num_err)
print(merror)