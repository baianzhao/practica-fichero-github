#Cines Paradiso celebran su décimo aniversario y por ser un día especial realizan importantes descuentos. A los adultos se les aplicará un 10% de descuento y a los menores de 18 años un 50%. Si la entrada cuesta 12 euros, calcula el total a pagar introduciendo por teclado el número de menores y el número de adultos que asisten al cine.
menores=int(input('introduzca el numero de menores'))
adultos=int(input('introduzca el numero de adultos'))
pmenores=12*50/100
pmenores=pmenores*menores
padultos=12*90/100
padultos=padultos*adultos
total=padultos+pmenores
pmenores=round(pmenores, 2)
padultos=round(padultos, 2)
total=round(total, 2)
print('El precio total del cine para ', menores,' menor/es es:',pmenores)
print('El precio total del cine para ', adultos,' adulto/s es:',padultos)
print('en total costara:',total,'euros')
