#A partir del programa anterior, modifica el código para que al introducir la letra por teclado te 
#indique en qué posición de la palabra se encuentra la letra.

ps=input('introduce la palabra secreta')
lenps=len(ps)
print('tienes ',lenps,' intentos para introducir letras')
pos=0

for x in range(lenps):
    let=input('introduce una letra')
    if let in ps:
            print('la letra existe')
            for i in range(lenps):
                if ps[i]==let:
                    print('la letra esta en la posicion: ',i+1)
    else:
            print('la letra no exisite')
        
