# numero =1

# while numero < 100 :
#     print(numero)
#     numero*= 2

comando = ""

# while comando != "salir":
#     comando = input("$ ")
#     print(comando)



import tkinter as tk
from tkinter import messagebox, simpledialog

root = tk.Tk()
root.withdraw()  # oculta la ventana principal

comando = ""

while comando != "salir":
    comando = simpledialog.askstring("Comando", "Ingresa un comando:")

    if comando is None:
        break  # si cierras la ventana

    if comando != "salir":
        messagebox.showinfo("Comando ingresado", comando)

messagebox.showinfo("Fin", "Programa terminado")