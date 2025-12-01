#Repite el ejercicio 63. En lugar de ‘tirar’ 100 veces un dado, modifica el programa para ver cómo
#se comporta el dado en lanzamientos producidos durante aprox 3 segundos. 

import random
import time
uno = dos = tres = cuatro = cinco = seis = 0

ini= time.time()


while time.time() - ini < 3:
    cara = random.randint(1, 6)

    if cara == 1:
        uno += 1
    elif cara == 2:
        dos += 1
    elif cara == 3:
        tres += 1
    elif cara == 4:
        cuatro += 1
    elif cara == 5:
        cinco += 1
    else:
        seis += 1

tiempo_total = time.time() - ini

# Mostrar resultados en formato del enunciado
print("RESUMEN")
print("Tiempo:", tiempo_total)
print("Uno:", uno)
print("Dos:", dos)
print("Tres:", tres)
print("Cuatro:", cuatro)
print("Cinco:", cinco)
print("Seis:", seis)
