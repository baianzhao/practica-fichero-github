#Asigna a una variable de texto la siguiente frase: A quién madruga Dios ayuda. Comprueba si existen las siguientes palabras mostrando por pantalla la posición de su índice
palcomp='A quién madruga Dios ayuda'
pal=input('introduce')
find=palcomp.find(pal)
if find>=0:
    print('la palabra esta en la frase. esta en la posicion :',find)
else:
    print('no esta en la frase')
