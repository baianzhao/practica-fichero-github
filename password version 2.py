#mostrar por pantalla todas las instrucciones
print('INSTRUCCIONS')#mostrar todas las instrucciones y requisitos de las contraseñas.
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
num_err=0#el numero de errores en la contraseña.
merror=''#el texto de los errores que se va a mostrar.
#detectar el numero de caracteres en la contraseña introducida por el usuario.
password_lenth=len(password)#detectar la longitud.
if password_lenth < 6 or password_lenth > 8:#si la longitud del password es superior a 8 o inferior a 6, directamente muestra error.
    num_err=1
    print(f'Error, el password té una longitud de {password_lenth} caràcters i no compleix els requisits')#mostrar error.
else:#si cumple la longitud, entonces, asignar variables de cada caracter con el caracter de la posicion correspondiente.
    n1=password[0]
    n2=password[1]
    n3=password[2]
    n4=password[3]
    n5=password[4]
    n6=password[5]
    #detectar si se tiene que crear mas variables para las posiciones opcionales 7 o 8.
    if password_lenth==7:
        n7=password[6]
    elif password_lenth==8:
        n7=password[6]
        n8=password[7]

#n1
    if not n1.isnumeric()==True or not int(n1)<=5 or not int(n1)>=1: #si el caracter 1 no cumple con las condiciones de ser un numero y ser del 1 al 5.
        num_err=num_err +1#si no es, directamente error.
        merror=merror+'/Error en el caracter 1/'
        
#n2       
    if n2.isalpha()==False or n2.islower()==False: #ver si cumple con la condicion de ser una letra y que sea minuscula
        num_err=num_err+1#si no es, directamente error.
        merror=merror+'/Error en el caracter 2/'

#n3   
    if n3.isalpha()!=True or n3.isupper()!=True: #ver si es una letra y si es mayuscula
        num_err=num_err +1#si no es, directamente error.
        merror=merror+'/Error en el caracter 3/'
    
#n4 
    if n4 not in '*_@':#detectar si en caracter 4 esta dentro de los simbolos
       num_err=num_err +1#error mas 1
       merror=merror+'/Error en el caracter 4/' 
    
#n5    
    if n5.isalpha()!=True or n5.islower()!=True: # ver si es una letra y si es minuscula(no mayuscula)
        num_err=num_err +1#si no es, directamente error.
        merror=merror+'/Error en el caracter 5/'

#n6
    if not n6.isnumeric()==True or not int(n6)<=9 or not int(n6)>=6: #ver si es un numero y si esta entre 6 y 9.
        num_err=num_err +1#si no es, directamente error.
        merror=merror+'/Error en el caracter 6/'

#n7    # se añade un condicional mas, para detectar si la longitud del password es mayor de 6.
    if password_lenth==7 or password_lenth==8:#ver la posicion 4 del password, consiste en lo mismo solo cambiando los signos.
        if n7 not in '&/#':#detectar si caracter 7 esta en esos simbolos.
            num_err=num_err +1
            merror=merror+'/Error en el caracter 7/' 

#n8    #se añade un condicional mas para ver si son 8 caracteres.
    if password_lenth==8:#ver posicion 1, es lo mismo.
        if n8.isnumeric()==False:
            num_err=num_err +1
            merror=merror+'/Error en el caracter 8/'
        else:
            if int(n8) > 5:
                num_err=num_err +1
                merror=merror+'/Error en el caracter 8/'

#Mostrar en pantalla si la contraseña es corresta o si es incorrecta, tambien mostrar los errores y en que posicion.
if num_err== 0:#si el numero de errores es 0, significa que el password esta bien y no tiene errores.
    print('El format del PASSWORD és correcte')#no hay error
else:
    print(merror)# los errores y sus posiciones. 'merror' significa 'mensaje error'.
    print('el numero total de errores es de: ',num_err)#mostrar el numero de errores.