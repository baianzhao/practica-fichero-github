#69. Realiza un programa que permita introducir una cantidad exacta de números, cada número se 
#irá almacenando en una lista. El programa debe finalizar presentando por pantalla los números 
#ordenados de menor a mayor.


cn=int(input('introduce la cantidad de numeros que quiere introducir'))
l=[]
for m in range(cn):
    a=int(input('introduce numero'))
    l.append(a)

print(l)