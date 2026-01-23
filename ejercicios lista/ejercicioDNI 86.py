#Diseñar un programa que al introducir un número calcule la letra correspondiente, teniendo en cuenta los
#siguientes puntos:
#Controlar que el valor introducido tenga una longitud de 8 dígitos y sea numérico.
#Visualizar el NIF completo, concatena la letra correspondiente separado con un guion: ej 11111111-R
#Controlar aquellas situaciones en que el Resto obtenido de un DNI no aparece en la tabla, por tanto, es
#incorrecto. Debe aparecer un mensaje de error.
#Por cada cálculo que se realice, el programa debe ofrecer la opción de continuar o no, introduciendo
#las letras “s” o “n”. En caso de seleccionar “n” se visualiza MENÚ del apartado 7.



resto=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
l='T,R,W,A,G,M,Y,F,P,D,X,B,N,J,Z,S,Q,V,H,L,C,K,E'
letras=l.split(',')
s='s'
lista_intentos=[]
dni_inc,dni_corr=[],[]

dni_iniciales,dni_final=[],[]
merr=[]
while s=='s':
    nerr=0
    dni=input('introduce tu DNI')
    DNI=[ch for ch in dni]
    lf=DNI[-1]
    dni_iniciales.append(dni)
    dni_num_part=dni[:-1]
    dni_num_part=int(dni_num_part)
    
#detectar errores
    #longitud
    if len(DNI)!=8:
        nerr+=1
        merr.append('/error longitud/')
    #deteccion de letras o numeros
    for x in str(dni_num_part):
        if x.isnumeric()!=True:
            nerr+=1
        else:
            nerr=nerr
        
    int(dni_num_part)
    #averiguar el resto
    rest=dni_num_part % 23

    #detectar si el resto esta dentro de lista
    if int(rest) not in resto:
        nerr+=0
    
    #detectar si la letra es correcta
    if lf!=letras[int(rest)]:
        nerr+=1
        merr.append('/letra incorrecta/')
    else:
        nerr=nerr

    
    #resultado correcto o no
    if nerr>=1:
        dni_inc.append(dni)
    elif nerr==0:
        dni_corr.append(dni)
    
    s=input('desea continuar? s/n')
    break
    

print(nerr)
print(rest)
print(dni_num_part)
print(DNI)
print(f'{dni_num_part}-{lf}')
