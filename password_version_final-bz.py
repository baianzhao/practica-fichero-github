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
    if n1.isalpha()== True:#detectar si es una letra, is es verdadero, directament error, ya que te pide un numero.
        num_err=num_err+1#sumar 1 al numero de errores.
        merror=merror+'/Error en el carácter 1/'#sumar el mensaje que quieres al mensaje anterior, asi, en cadena.
    else:
        if int(n1)>5 or int(n1)<1:#si antes se detecta que no es una letra, se entiende que es un numero, y por lo tanto, detectar si esta dentro del rango de 1 a 5.
            num_err=num_err+1#numero de errores mas 1.
            merror=merror+'/Error en el carácter 1/'#si no esta, entonces, mostrar error.
        
#n2
    if n2.isalpha()==False:#detectar si es una letra alfabetica.
        num_err=num_err +1#si no es, directamente error.
        merror=merror+'/Error en el caracter 2/'

    else:
        if n2.islower() == False:#si anteriormente, se detecta que es una letra, entonces, detectar si es mayuscula o minuscula.
            num_err=num_err +1#sumar numero de errores mas 1.
            merror=merror+'/Error en el caracter 2/'#si no es minuscula, error.

#n3
    if n3.isalpha()== False:#detectar si es una letra o no.
        num_err=num_err +1
        merror=merror+f'/Error en el caracter 3/'#si no es letra, directamente error.
    else:
        if n3.isupper() == False:#si es letra, entonces detectar si es mayuscula o no.
            num_err=num_err +1
            merror=merror+'/Error en el caracter 3/'#si es, entonces nada, si no es, entonces error.
    
#n4
    s41=n4.find('*' or '_' or '@')#buscar si en esa posicion hay uno de esos signos, te devuelve un numero, si es 0, es que no hay.
    if s41 >0:#si no hay uno de esos simbolos, error.
       num_err=num_err +1
       merror=merror+'/Error en el caracter 4/' 
    
#n5
    if n5.isalpha()==False:#ver la posicion 2, es lo mismo.
        num_err=num_err +1
        merror=merror+'/Error en el caracter 5/'

    else:
        if n5.islower() == False:
            num_err=num_err +1
            merror=merror+'/Error en el caracter 5/'

#n6
    if n6.isnumeric()== False:#ver la posicion 1 del password. es lo mismo.
        num_err=num_err +1
        merror=merror+'/Error en el caracter 6/'
    else:
        if int(n6) >9 or int(n6)< 6:
            num_err=num_err +1
            merror=merror+'/Error en el caracter 6/'

#n7    # se añade un condicional mas, para detectar si la longitud del password es mayor de 6.
    if password_lenth==7 or password_lenth==8:#ver la posicion 4 del password, consiste en lo mismo solo cambiando los signos.
        s71=n7.find('&' or '/' or '#')
        if s71 >0:
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

