#Realiza un programa que introduzcas por teclado una palabra ‘secreta’, consigue la longitud de 
#esa palabra para que sea ese el criterio que establezca el rango del bucle de manera que el usuario
#tenga x oportunidades para ver si letra introducida está en esa palabra.

ps=input('introduce la palabra secreta')
lenps=len(ps)
print('tienes ',lenps,' intentos para introducir letras')

for n in range(lenps):
    psp=input('introduce una letra')
    if psp in ps:
        print('la letra existe')
    else:
        print('la letra no exsiste')
    
