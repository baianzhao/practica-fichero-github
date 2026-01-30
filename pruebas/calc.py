import tkinter as tk

ventana = tk.Tk()
ventana.title("Calculadora Básica")
ventana.geometry("400x350")

def sumar():
    try:
        num1 = float(campo_num1.get())
        num2 = float(campo_num2.get())
        resultado = num1 + num2
        etiqueta_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        etiqueta_resultado.config(text="Error: Ingresa números válidos")

def restar():
    try:
        num1 = float(campo_num1.get())
        num2 = float(campo_num2.get())
        resultado = num1 - num2
        etiqueta_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        etiqueta_resultado.config(text="Error: Ingresa números válidos")

def multiplicar():
    try:
        num1 = float(campo_num1.get())
        num2 = float(campo_num2.get())
        resultado = num1 * num2
        etiqueta_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        etiqueta_resultado.config(text="Error: Ingresa números válidos")

def dividir():
    try:
        num1 = float(campo_num1.get())
        num2 = float(campo_num2.get())
        if num2 == 0:
            etiqueta_resultado.config(text="Error: No se puede dividir por cero")
        else:
            resultado = num1 / num2
            etiqueta_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        etiqueta_resultado.config(text="Error: Ingresa números válidos")

def potencia():
    try:
        num1 = float(campo_num1.get())
        num2 = float(campo_num2.get())
        resultado = num1 ** num2
        etiqueta_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        etiqueta_resultado.config(text="Error: Ingresa números válidos")

# Título
tk.Label(ventana, text="CALCULADORA BÁSICA", font=("Arial", 16, "bold")).pack(pady=10)

# Primer número
tk.Label(ventana, text="Primer número:", font=("Arial", 12)).pack(pady=5)
campo_num1 = tk.Entry(ventana, font=("Arial", 12), width=20, justify="center")
campo_num1.pack(pady=5)

# Segundo número
tk.Label(ventana, text="Segundo número:", font=("Arial", 12)).pack(pady=5)
campo_num2 = tk.Entry(ventana, font=("Arial", 12), width=20, justify="center")
campo_num2.pack(pady=5)

# Frame para organizar los botones en filas
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=20)

# Primera fila de botones
boton_suma = tk.Button(frame_botones, text="+ Sumar", command=sumar, bg="lightgreen", width=10)
boton_suma.grid(row=0, column=0, padx=5, pady=5)

boton_resta = tk.Button(frame_botones, text="- Restar", command=restar, bg="lightcoral", width=10)
boton_resta.grid(row=0, column=1, padx=5, pady=5)

boton_multiplicar = tk.Button(frame_botones, text="× Multiplicar", command=multiplicar, bg="lightblue", width=10)
boton_multiplicar.grid(row=0, column=2, padx=5, pady=5)

# Segunda fila de botones
boton_dividir = tk.Button(frame_botones, text="÷ Dividir", command=dividir, bg="lightyellow", width=10)
boton_dividir.grid(row=1, column=0, padx=5, pady=5)

boton_potencia = tk.Button(frame_botones, text="^ Potencia", command=potencia, bg="plum", width=10)
boton_potencia.grid(row=1, column=1, padx=5, pady=5)

# Resultado
etiqueta_resultado = tk.Label(ventana, text="Resultado aparecerá aquí", 
                             font=("Arial", 14, "bold"), bg="white", 
                             relief="sunken", width=30, height=2)
etiqueta_resultado.pack(pady=20)

ventana.mainloop()