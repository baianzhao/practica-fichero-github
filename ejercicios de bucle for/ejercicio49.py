#A partir del programa anterior, modifica el código para que al introducir la letra por teclado te 
#indique en qué posición de la palabra se encuentra la letra.

ps=input('introduce la palabra secreta')
lenps=len(ps)
print('tienes ',lenps,' intentos para introducir letras')

for n in range(lenps):
    psp=input('introduce una letra')
    if psp in ps:
        print('la letra existe')
        n=str(n)
        pos=ps.count(n)
        print(pos)
        
        
        
    else:
        print('la letra no exsiste')
        