import random
Lista_palabrasecreta=['perro','gato','agua','tiburon','manzana','reloj','ordenador','casa','python','minecraft']
Lista_partida=[]
Lista_ahorcado=[]
palabra_sec=random.choice(Lista_palabrasecreta)
pal_sec_splited=[ch for ch in palabra_sec]
n_guiones=len(palabra_sec)
guiones=[]
for x in range(n_guiones):
    guiones.append('_')
    guiones.append(',')
guiones.pop()
print('[',*guiones,']')
print(guiones)