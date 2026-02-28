import random
import time
from datetime import datetime
import os
sino=False
Lista_palabrasecreta=['perro','gato','agua','tiburon','manzana','reloj','ordenador','casa','python','minecraft']
completo,n_partidas=0,0
while completo==0:
    sino=False
    Lista_partida=[]
    Lista_ahorcado=[]
    Lista_err,lista_acc=[],[]
    palabra_sec=random.choice(Lista_palabrasecreta)
    pal_sec_splited=[ch for ch in palabra_sec]
    posicion=-1
    for n in pal_sec_splited:
        posicion+=1
        if n in 'áÁ':
            pal_sec_splited[posicion]='a'
        if n in 'éÉ':
            pal_sec_splited[posicion]='e'
        if n in 'Íí':
            pal_sec_splited[posicion]='i'
        if n in 'óÓ':
            pal_sec_splited[posicion]='o'
        if n in 'úÚ':
            pal_sec_splited[posicion]='u'
    n_guiones=len(palabra_sec)
    pal_ahorc=['A','H','O','R','C','A','D','O']
    for x in range(n_guiones):
        Lista_partida.append('_')
        Lista_partida.append(',')
    Lista_partida.pop()
    print('[',*Lista_partida,']')
    ini=time.time()
    err=0
    while sino==False:
        p=-2
        list_pos=[]
        inp=input('introduce la letra: ').lower()
        if len(inp) != 1 or not inp.isalpha():
            print("Error: Por favor, introduce solo una letra válida.")
            continue
        if inp in pal_sec_splited:
            if  inp in Lista_partida:
                print('la letra ya está usada')
            else:
                for x in pal_sec_splited:
                    p+=2
                    if inp==x:
                        Lista_partida[p]=inp
                        lista_acc.append(inp)
            print('[',*Lista_partida,']')
        else:
            Lista_ahorcado.append(pal_ahorc[err])
            err+=1
            print(*Lista_ahorcado)
            Lista_err.append(inp)
            print('[',*Lista_partida,']')
            if err==8:
                sino=True
                tf=time.time()
                t_usado=tf-ini
                t_usado=round(t_usado, 2)
                t_min=t_usado//60
                t_seg=t_usado%60
                print('No has acertado la palabra correcta, la palabra secreta era: ',palabra_sec)    
        if '_' not in Lista_partida:
            sino=True
            tf=time.time()
            t_usado=tf-ini
            t_usado=round(t_usado, 2)
            t_min=t_usado//60
            t_seg=t_usado%60
            t_min,t_seg=round(t_min),round(t_seg)
            print('enhorabuena!!, has acertado!!')      

    Lista_palabrasecreta.remove(palabra_sec)
    n_partidas+=1
    print()
    print('*'*5,'ESTADISTICAS','*'*5)
    print(len(Lista_err),' error/es en total')
    print(len(lista_acc),' acierto/s en total')
    print(f'ha usado {t_min} minutos y {t_seg} segundos para completar la palabra') 
    print(f'ha jugado {n_partidas} partida/s')

    if len(Lista_palabrasecreta)==0:
        print('eres un crack! has adivinado todas las palabras!!!')
        completo=1
        seguir=1
        print('programa finalizado')
        break
     

    ahora = datetime.now()  
    fecha_formateada = ahora.strftime("%d/%m/%Y %H:%M:%S")
    contenido=f'{fecha_formateada}/{palabra_sec}/numero de errores:{len(Lista_err)}/numero de aciertos:{len(lista_acc)}'

    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_archivo = os.path.join(directorio_actual, "text.txt")
    with open(ruta_archivo, "a", encoding="utf-8") as archivo:
        archivo.write(contenido + "\n")
        archivo.flush() 
        
    impcorr=0
    while impcorr==0:
        print('¿desea añadir palabra nueva? s/n')
        sn_new_w=input()
        if sn_new_w=='s' or sn_new_w=='S':
            nw=input('introduce palabra nueva: ')
            nw=nw.lower()
            Lista_palabrasecreta.append(nw)
            print(f'¡se ha añadido la palabra "{nw}" correctamente!')
            impcorr=1
        elif sn_new_w=='n' or sn_new_w=='N':
            print('no se ha añadido palabra')
            impcorr=1
        else:
            impcorr=0
    seguir=0
    while seguir==0:
        print('¿desea seguir? s/n')
        sn=input()
        if sn=='n'or sn=='N':
            completo=1
            seguir=1
            print('programa finalizado')
        elif sn=='s' or sn=='S':
            completo=0
            print('siguiente ronda')
            seguir=1
        else:
            seguir=0
