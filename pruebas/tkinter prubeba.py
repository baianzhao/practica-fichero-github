import tkinter as tk
from tkinter import ttk
root=tk.Tk()

root.title('hola')
root.attributes('-alpha', 1)
root.configure(bg='blue')
root.config(cursor='watch')
txt=tk.Label(root, text='dale click al boton', 
             bg='red', 
             fg='yellow',
             cursor='plus',
             font=('Calibri, 16')
             )
txt.pack()
btn=ttk.Button(root, 
               text='exit', 
               command=lambda:root.quit(),
               cursor='arrow',
                )

btn.pack()
root.attributes('-fullscreen', False)
root.geometry('600x200')




root.mainloop()