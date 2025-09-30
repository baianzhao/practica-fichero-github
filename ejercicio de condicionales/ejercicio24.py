#Corrige los errores del siguiente código y comprueba que se ejecuta correctamente
var1=float(input('introduce el peso: '))#la variable no puede empezar por un numero
var2=float(input('introduce la altura: '))#variable mal asignada, tambien hay que añadir el float, o si no, la altura te la detecta como string
var_imc=var1/var2**2 # para asignar variable solo un signo igual.
print('si pesas ',var1,' kilos y mides ',var2,'tu IMC es: ',var_imc)#para incluir valor de variables al texto hay que poner comas.
if var_imc>25:#falta el signo':'
    print('hay sobrepeso')
else:
    print('estas dentro de los parametros normales')