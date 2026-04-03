# n1 = input("ingesa un numro")
# n2 = input("ingesa un numro")

# n1 = int(n1)
# n2 = int(n2)

# suma = n1 +n2
# resta = n1-n2
# multi = n1* n2
# div = n1 / n2 

# mensaje = f""" para los numeros ingresados {n1} y  {n2} 
# el resultado de la suma es {suma}
# el resultado de la resta es {resta}
# el resultado de la multiplicación es {multi}
# el resultado de la división es {div}
# """

# print(mensaje)


import tkinter as tk
from tkinter import simpledialog

root = tk.Tk()
root.withdraw()

nombre = simpledialog.askstring("Input", "Ingresa tu nombre:")
print(nombre)