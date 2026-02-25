import random
import time
def leer_txt_como_lista(ruta_archivo):
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            # strip() elimina saltos de línea y espacios extra
            lista = [linea.strip() for linea in archivo if linea.strip()]
        return lista
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{ruta_archivo}'.")
        return []
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return []


ruta = 
lista_datos = leer_txt_como_lista(ruta)
sino=False
Lista_palabrasecreta=[lista_datos]
completo=0
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
        inp=input('introduce la letra: ')
        inp=inp.lower()
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
        if '_' not in Lista_partida:
            sino=True
            tf=time.time()
            t_usado=tf-ini
            t_usado=round(t_usado, 2)
            print(f'ha usado {t_usado} segundos para completar la palabra')
            
    print('¿desea añadir palabra nueva? s/n')
    sn_new_w=input()
    if sn_new_w=='s':
        nw=input('introduce palabra nueva: ')
        nw=nw.lower()
        Lista_palabrasecreta.append(nw)
        print(f'¡se ha añadido la palabra {nw} correctamente!')
    
    print('¿desea seguir? s/n')
    sn=input()
    if sn=='n':
        print('programa finalizado')
        print(len(Lista_err),' error/es en total')
        print(len(lista_acc),' acierto/s en total')
        completo=1
    elif sn=='s':
        completo=0
        print('siguiente ronda')

