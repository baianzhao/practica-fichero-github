#Corrige los 4 errores o añade el código que necesites para que el siguiente programa se ejecute correctamente.-------V2

#inicializo valores a cada variable
var_numero=input(str('introduce un numero de 4 digitos'))#he añadido la funcion de que el usuario pueda interactuar
var_suma=float(0)
#obtengo su longitud
var_longitud=len(str(var_numero))
if var_longitud==4:
    d1=float(var_numero[0])
    d2=float(var_numero[1])
    d3=float(var_numero[2])
    d4=float(var_numero[3])
    var_suma= float(d1+d2+d3+d4)
    print(var_suma)
    var_suma2=var_suma//2
    parono=var_suma%var_suma2
    if parono == 0:
        print ('el valor de ',var_suma,'es par')
    else:
        print('el valor de ',var_suma,'es impar') 
else:
    print('el numero no es de 4 digitos')
