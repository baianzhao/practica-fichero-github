import tkinter as tk
from tkinter import ttk
root=tk.Tk()
root.title('ventana random')
msg=tk.Label(root, text= 'hola')
msg.pack()
t=tk.Label(root, text='eres tonto?')
t.pack()
root.geometry('500x500')
root.resizable(False, False)



button1=ttk.Button(root, text='click', command=lambda: root.quit())
root.mainloop()
