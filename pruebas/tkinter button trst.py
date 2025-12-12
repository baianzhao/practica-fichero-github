import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.geometry('400x200+50+50')
button=ttk.Button(root, text='click para cerrar', command=lambda:root.quit()
                  ,width=30)


button.pack()
root.mainloop()