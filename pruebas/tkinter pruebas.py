import tkinter as tk

root = tk.Tk()


root.title('Tkinter prueba 3')
root.geometry('400x100')
msg=tk.Label(root, text='prueba 3 de tkiner para dominar ventanas')
root.attributes('-alpha', 1)
msg.pack()



root.mainloop()