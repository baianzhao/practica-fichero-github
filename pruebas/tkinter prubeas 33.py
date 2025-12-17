import tkinter as tk
root=tk.Tk()
root.geometry('600x600')
msg=tk.Label(root, text='hola')
root.config(cursor="watch")
root.title('hello test 1')
root.attributes('-alpha', 1)
msg.pack()

from tkinter import ttk
Buton=ttk.Button(root, text='adios', command=lambda:root.quit())

Buton.pack()


root.mainloop()