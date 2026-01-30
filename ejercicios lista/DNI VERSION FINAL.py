#Diseñar un programa que al introducir un número calcule la letra correspondiente, teniendo en cuenta los
#siguientes puntos:
#Controlar que el valor introducido tenga una longitud de 8 dígitos y sea numérico.
#Visualizar el NIF completo, concatena la letra correspondiente separado con un guion: ej 11111111-R
#Controlar aquellas situaciones en que el Resto obtenido de un DNI no aparece en la tabla, por tanto, es
#incorrecto. Debe aparecer un mensaje de error.
#Por cada cálculo que se realice, el programa debe ofrecer la opción de continuar o no, introduciendo
#las letras “s” o “n”. En caso de seleccionar “n” se visualiza MENÚ del apartado 7.
l='T,R,W,A,G,M,Y,F,P,D,X,B,N,J,Z,S,Q,V,H,L,C,K,E'#lista de las letras de los dnis
letras=l.split(',')#usar split para facilitar(no tener que poner comillas a cada letra)
s,ert,errores,ell,eaa,ett='s',0,0,0,0,0
dni_inc,dni_corr,dni_iniciales,dni_final,lista_intentos,resto=[],[],[],[],[],[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
while s=='s':#mientrar la respuesta del bucle sea [s] de si, repetir las introducciones
    nerr=0
    let_dni=''
    dni=input('introduce tu DNI')#introduccion del dni.
    DNI=[ch for ch in dni]#separacion de los numeros o caracteres.
    dni_iniciales.append(dni)
    merr=[]#mensaje de error definitivo que se muestra
    for x in str(dni):
        if x.isnumeric()!=True:#mirar si son caracteres o numeros
            nerr+=1
            ert+=nerr
        else:
            nerr=nerr#no hacer nada(basicamente)
    if nerr==0:
        dni=int(dni)  #si no se detecta errores, el dni es valido, y por tanto, todos son numeros.
    #detectar errores
        #longitud
        if len(DNI)!=8:#de nuevo, 
            nerr+=1
            ert+=nerr
            merr.append('/error longitud/')#añadir mensaje de error.
            lista_intentos.append(0)
        #deteccion de letras o numeros
        for x in str(dni):
            if x.isnumeric()!=True:#detectar que no es numerico
                nerr+=1
                ert+=nerr
            else:
                nerr=nerr
        int(dni)
        #averiguar el resto
        rest=dni % 23
        #detectar si el resto esta dentro de lista
        if int(rest) not in resto:
            nerr+=1
            ert+=nerr
            merr.append('/el DNI no existe/')#error imposible
            lista_intentos.append(2)
        else:
            #averiguar letra
            if len(DNI)==8:#se mide la longitud de los numeros de dni.
                nerr=nerr
                let_dni=letras[int(rest)]
        #resultado correcto o no
                dni_f=f'{dni}-{let_dni}'#dni definitivo, con la letra y el guion.
            else:
                dni_f=dni
        if nerr!=0:
            dni_inc.append(dni_f)#añadir dni a la lista de dnis incorrectos
            
        elif nerr==0:#si no hay errores:
            dni_corr.append(dni_f)#append dni a la lista de correctos.
            lista_intentos.append(3)#a la lista de intentos, poner un 3.
            print(dni_f)#mostrar dni final(en caso de correcto)
#errores
    else:#detectar tipos de errores
        el,ea,et,er=0,0,0,0#error longitud, error alpha, error todo(longitud y alpha), error para recorrer todo el dni
        dni_inc.append(dni)#como es incorrecto, se añade a la lista de incorrectos
        nerr+=1
        ert+=nerr
        if len(DNI)!=8:#error de longitud
            el+=1
        for z in DNI:#error de caracteres que no son numeros
            if z.isalpha()==True:
                er+=1
        if er>0:
            ea+=1
        if el==1:
            merr.append('/error longitud/')#append a mensaje de error el texto.
            lista_intentos.append(0)
        if ea==1:
            merr.append('/error letras/')#mensaje de error de letras
            lista_intentos.append(1)
        if el==1 and ea==1:
            et+=1
        ell+=el#total de errores
        eaa+=ea
        ett+=et
    if nerr>0:
        print(merr)#mostrar los errores(mensajes)
    s=input('desea continuar? s/n')
    if s=='n':
        break
print('programa finalizado')#mensaje de programa final
errores=len(dni_inc)#sacar dnis incorrectos
corr=len(dni_corr)#sacar total de dnis correctos
dni_corr.sort()
dni_final.sort()
#mostrar
print(dni_corr)#mostrar la lista de dnis correctos
print(dni_inc)#mostrar los dnis incorrectos
print('el numero de errores es de:',errores)#mostrar numero de errores(dnis incorrectos)
print('el numero de DNIs correctos es de:',corr)#mostrar dnis correctos
print('el numero de intentos es de:',len(dni_inc)+len(dni_corr))#sumar el numero total de dnis introducidos
print('el porcentaje de los DNIs correctos es de:',round(corr/(len(dni_inc)+len(dni_corr))*100, 2),' %')#mostrar porcentajes
print('el porcentaje de los DNIs incorrectos es de:',round(errores/(len(dni_inc)+len(dni_corr))*100, 2),' %')#mostrar porcentajes
print('el porcentaje de los fallos de longitud es de:',round(ell/(len(dni_inc)+len(dni_corr))*100, 2),' %')#mostrar porcentajes
print('el porcentaje de los fallos de letras es de:',round(eaa/(len(dni_inc)+len(dni_corr))*100, 2),' %')#mostrar porcentajes
print('el porcentaje de los fallos en tanto las letras como en la longitud es de:',round(ett/(len(dni_inc)+len(dni_corr))*100, 2),' %')#mostrar porcentajes de los 2 tipos
print(lista_intentos)#mostrar lista intentos: 0,1,2,3
