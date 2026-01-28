#Diseñar un programa que al introducir un número calcule la letra correspondiente, teniendo en cuenta los
#siguientes puntos:

#Controlar que el valor introducido tenga una longitud de 8 dígitos y sea numérico.
#Visualizar el NIF completo, concatena la letra correspondiente separado con un guion: ej 11111111-R
#Controlar aquellas situaciones en que el Resto obtenido de un DNI no aparece en la tabla, por tanto, es
#incorrecto. Debe aparecer un mensaje de error.
#Por cada cálculo que se realice, el programa debe ofrecer la opción de continuar o no, introduciendo
#las letras “s” o “n”. En caso de seleccionar “n” se visualiza MENÚ del apartado 7.
import tkinter as tk
from tkinter import ttk

ventana=tk.Tk()
ventana.geometry('300x300')
txt1=tk.Label(ventana, text='INTRODUCE TU NUMERO DE DNI')
txt1.pack()
intro=tk.Entry(ventana)
intro.pack()
def obtener_texto():
    texto = intro.get()
    print(f"Texto ingresado: {texto}")


ventana.mainloop()























l='T,R,W,A,G,M,Y,F,P,D,X,B,N,J,Z,S,Q,V,H,L,C,K,E'
letras=l.split(',')
s,ert,errores,ell,eaa,ett='s',0,0,0,0,0
dni_inc,dni_corr,dni_iniciales,dni_final,lista_intentos,resto=[],[],[],[],[],[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
while s=='s':
    nerr=0
    let_dni=''
    dni=input('introduce tu DNI')
    DNI=[ch for ch in dni]
    dni_iniciales.append(dni)
    merr=[]
    for x in str(dni):
        if x.isnumeric()!=True:
            nerr+=1
            ert+=nerr
        else:
            nerr=nerr
    if nerr==0:
        dni=int(dni)  
    #detectar errores
        #longitud
        if len(DNI)!=8:
            nerr+=1
            ert+=nerr
            merr.append('/error longitud/')
            lista_intentos.append(0)
        #deteccion de letras o numeros
        for x in str(dni):
            if x.isnumeric()!=True:
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
            if len(DNI)==8:
                nerr=nerr
                let_dni=letras[int(rest)]
        #resultado correcto o no
                dni_f=f'{dni}-{let_dni}'
            else:
                dni_f=dni
        if nerr!=0:
            dni_inc.append(dni_f)
            
        elif nerr==0:
            dni_corr.append(dni_f)
            lista_intentos.append(3)
            print(dni_f)
#errores
    else:
        el,ea,et,er=0,0,0,0
        dni_inc.append(dni)
        nerr+=1
        ert+=nerr
        if len(DNI)!=8:
            el+=1
        for z in DNI:
            if z.isalpha()==True:
                er+=1
        if er>0:
            ea+=1
        if el==1:
            merr.append('/error longitud/')
            lista_intentos.append(0)
        if ea==1:
            merr.append('/error letras/')
            lista_intentos.append(1)
        if el==1 and ea==1:
            et+=1
        ell+=el
        eaa+=ea
        ett+=et
    if nerr>0:
        print(merr)
    s=input('desea continuar? s/n')
    if s=='n':
        break
print('programa finalizado')
errores=len(dni_inc)
corr=len(dni_corr)
dni_corr.sort()
dni_final.sort()
#mostrar
print(dni_corr)
print(dni_inc)
print('el numero de errores es de:',errores)
print('el numero de DNIs correctos es de:',corr)
print('el numero de intentos es de:',len(dni_inc)+len(dni_corr))
print('el porcentaje de los DNIs correctos es de:',round(corr/(len(dni_inc)+len(dni_corr))*100, 2),' %')
print('el porcentaje de los DNIs incorrectos es de:',round(errores/(len(dni_inc)+len(dni_corr))*100, 2),' %')
print('el porcentaje de los fallos de longitud es de:',round(ell/(len(dni_inc)+len(dni_corr))*100, 2),' %')
print('el porcentaje de los fallos de letras es de:',round(eaa/(len(dni_inc)+len(dni_corr))*100, 2),' %')
print('el porcentaje de los fallos en tanto las letras como en la longitud es de:',round(ett/(len(dni_inc)+len(dni_corr))*100, 2),' %')
print(lista_intentos)
