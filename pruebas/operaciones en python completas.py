import math
var1=float(input('introduce un numero'))
var2=float(input('introduce otro numero'))
totalsum=var1+var2
totalrest=var1-var2
totalmult=var1*var2
totaldiv=var1/var2
totalpot=var1**var2
totalraiz1=math.sqrt(var1)
totalraiz2=math.sqrt(var2)
diventera=var1//var2
#mostrar valores finales
print('la suma de los valores es: ',totalsum)
print('la resta de los valores es: ',totalrest)
print('la multiplicacion de los valores es: ',totalmult)
print('la division de los valores es: ',totaldiv)
print('la potencia de valor 1 elevado a valor 2 de los valores es: ',totalpot)
print('la raiz quadrada de los dos valores son: ',totalraiz1, 'y', totalraiz2)
print('la div. entera es', diventera)
#lista de los valores finales
for a in [ totalsum, totalrest, totalmult, totaldiv, totalpot, totalraiz1, totalraiz2,diventera]:
    print(a)
    