import random
sino=False
Lista_palabrasecreta=['perro','gato','agua','tiburon','manzana','reloj','ordenador','casa','python','minecraft','tetris','esternocleidomastoideo']
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
ac=0
err=0
while sino==False:
    p=-2
    list_pos=[]
    inp=input()
    inp=inp.lower()
    if inp in pal_sec_splited:
        for x in pal_sec_splited:
            p+=2
            if inp==x:
                Lista_partida[p]=inp
                ac+=1
        print('[',*Lista_partida,']')
    if ac==len(pal_sec_splited):
        break

    else:
        Lista_ahorcado.append(pal_ahorc[err])
        err+=1
        print(*Lista_ahorcado)
        print('[',*Lista_partida,']')
        if err==8:
            break

