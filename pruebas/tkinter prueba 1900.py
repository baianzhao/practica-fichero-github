import tkinter as tk

hola=tk.Tk()
uno=tk.Button(hola, text='adios',command=lambda:hola.quit())
hola.geometry('200x200')

texto=tk.Label(hola, text='¿Eres tonto??',bg='red',font='Arial, 12',padx=3, pady=5)

texto.pack()
uno.pack()

hola.config(bg='blue',
            cursor='star')
uno.config(cursor='watch')

hola.attributes('-alpha',1)

hola.mainloop()
