list=[1,2,3,4,5,6]
lista2=[]
max=max(list)
min=min(list)
suma=sum(list)

for n in list:
    num2=n*2
    lista2.append(num2)
    

listpro=[n*2 for n in list]


print(list)
print(f'valor maximo es:{max}')
print(f'valor minimo es:{min}')
print(f'la suma de los valores es:{suma}')
print(lista2)
print(listpro)










import time

import tkinter as tk
hola=tk.Tk()
hola.config(cursor='watch',bg='blue')
hola.attributes('-alpha', 0.3)
hola.attributes(fullscreen='True')



hola.mainloop()

def hola2():
    hola.config(bg='red')
    hola.mainloop()
    time.sleep(0.1)
    hola.config(bg='green')
    hola.mainloop()
    time.sleep(0.1)
    hola.config(bg='yellow')
    hola.mainloop()


hola2()
hola2()
hola2()
hola2()