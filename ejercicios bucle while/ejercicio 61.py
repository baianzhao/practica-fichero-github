#A partir del código anterior, haz que el programa finalice si el valor de la tabla de multiplicar es
#superior o igual a 40.

n=int(input('introduce un numero'))
ntm=1
res=0
tf=False
while tf==False:
    if res>=40:
        tf=True
        print('fin del programa')
    else:
        if ntm>10:
            tf=True
            print('fin del programa')
        else:
            res=n*ntm
            print(res)
            ntm+=1
