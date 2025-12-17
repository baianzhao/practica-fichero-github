import tkinter as tk
from tkinter import ttk
from tkinter.colorchooser import askcolor


root = tk.Tk()
root.title('Tkinter Color Chooser')
root.geometry('300x150')


def change_color():
    colors = askcolor(title="Tkinter Color Chooser")
    root.configure(bg=colors[1])


ttk.Button(
    root,
    text='tonto',
    command=change_color).pack(expand=True)
root.config(cursor='plus')


root.mainloop()