#Utiliza el método sqrt de la librería math para calcular la raíz cuadrada de un número. El resultado de la raíz cuadrada divídelo entre 2 de manera que se obtenga siempre un resultado entero. Haz que se muestre por pantalla los dos resultados de todo el proceso(raíz y división).
import math
num=int(input('introduce un numero'))
raiz=math.sqrt(num)
raiz2=raiz/2
raiz2=math.trunc(raiz2)
raiz=round(raiz, 2)
print('el resultado de la raiz es: ',raiz)
print('el resultado de division es: ',raiz2)
