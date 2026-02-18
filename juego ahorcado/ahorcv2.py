import random
sino=False
Lista_palabrasecreta=['perro','gato','agua','tiburon','manzana','reloj','ordenador','casa','python','minecraft']


while sino==False:
    Lista_partida=[]
    Lista_ahorcado=[]
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
    add=0
    while add==0:

        inp=input()
        if input in pal_sec_splited:
            print('si')

        else:
            Lista_ahorcado.append(pal_ahorc[err])
            err+=1
            print(*Lista_ahorcado)
            print('[',*Lista_partida,']')
            if err==8:
                break

print(Lista_partida)
