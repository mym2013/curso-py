# Calculadora interactiva acumulativa
#
# Este programa solicita un número inicial al usuario.
# Luego entra en un bucle donde:
# - Pide una operación (suma, resta, multi, div o salir)
# - Pide un nuevo número
# - Aplica la operación al resultado actual
# - Muestra el resultado
#
# El resultado de cada operación se guarda y se utiliza
# como base para la siguiente operación.
#
# El programa continúa hasta que el usuario escribe "salir".



#pedimos un par de nuemros para jugar 
# num1 = int(input( "dame un numero entero"))
# num2= int(input( "dame un numero entero"))

# pregunta = ""
# while pregunta!= "salir":
#     resultado = 0
#     pregunta = input("ingresa una operación sum,rest,multi,div o escribe salir para terminar", pregunta).lower()
#     if pregunta == "sum ":
#        resultado = num1 + num2 
#     elif  pregunta == "rest":  
#        resultado == num1 - num2 
#      elif  pregunta == "multi":
#         resultado == num1*num2
#     elif pregunta == "div":
#         resultado == num1/num2

#         print(resultado)
#     elif resultado == "salir"
#     break    
     

num1 = int(input("dame un numero entero: "))
num2 = int(input("dame otro numero entero: "))

pregunta = ""

while pregunta != "salir":
    resultado = 0
    pregunta = input("ingresa una operación sum, rest, multi, div o escribe salir: ").lower()

    if pregunta == "sum":
        resultado = num1 + num2 
        num1 = resultado
        num2 = int(input("dame otro numero entero: "))
    elif pregunta == "rest":  
        resultado = num1 - num2 
        num1 = resultado
        num2 = int(input("dame otro numero entero: "))
    elif pregunta == "multi":
        resultado = num1 * num2
        num2 = int(input("dame otro numero entero: "))
        num1 = resultado
    elif pregunta == "div":
        resultado = num1 / num2
        num2 = int(input("dame otro numero entero: "))
        num1 = resultado
    elif pregunta == "salir":
        break

    print(resultado)

