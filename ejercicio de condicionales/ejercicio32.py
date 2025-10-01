#Cómo solucionarías con ayuda de métodos String el problema del ejercicio anterior para no distinguir entre mayúsculas y minúsculas.

palcomp='a quién madruga dios ayuda'
pal=str(input('introduce la palabra'))
pal=pal.lower()
find=palcomp.find(pal)
if find>=0:
    print('la palabra esta en la frase. esta en la posicion :',find)
else:
    print('no esta en la frase')