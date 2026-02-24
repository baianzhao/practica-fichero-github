import random
sino=False
Lista_palabrasecreta=['perro','gato','agua','tiburon','manzana','reloj','ordenador','casa','python','minecraft','tetris','esternocleidomastoideo']
completo=0
while completo==0:
    sino=False
    Lista_partida=[]
    Lista_ahorcado=[]
    Lista_err,lista_acc=[],[]
    palabra_sec=random.choice(Lista_palabrasecreta)
    pal_sec_splited=[ch for ch in palabra_sec]
    n_guiones=len(palabra_sec)
    pal_ahorc=['A','H','O','R','C','A','D','O']

    for x in range(n_guiones):
        Lista_partida.append('_')
        Lista_partida.append(',')
    Lista_partida.pop()
    print('[',*Lista_partida,']')

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
    
    print('¿desea añadir palabra nueva? s/n')
    sn_new_w=input()
    if sn_new_w=='s':
        nw=input('introduce palabra nueva: ')
        nw=nw.lower()
        Lista_palabrasecreta.append(nw)
    
    print('¿desea seguir? s/n')
    sn=input()
    if sn=='n':
        print('programa finalizado')
        completo=1
    elif sn=='s':
        completo=0
        print('siguiente ronda')

