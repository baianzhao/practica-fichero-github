import random
sino=False
Lista_palabrasecreta=['perro','gato','agua','tiburon','manzana','reloj','ordenador','casa','python','minecraft']
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









































#while sino==False:
#    list_pos=[]
#    inp=input()
#    inp=inp.lower()
#    if inp in pal_sec_splited:
#        for x in pal_sec_splited:
#             if x==inp:
#                pos=pal_sec_splited.index(x)
#                list_pos.append(pos)
#                for y in list_pos:
#                    Lista_partida[pos]==inp
#            
#
#        print('[',*Lista_partida,']')
#    else:
#        Lista_ahorcado.append(pal_ahorc[err])
#        err+=1
#        print(*Lista_ahorcado)
#        print('[',*Lista_partida,']')
#        if err==8:
#            break
#print(pos)
#print(Lista_partida)
