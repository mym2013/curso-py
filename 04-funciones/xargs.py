# def suma(*numeros):# a esto se le llamam XARGS , equis argumentos
#     resultado = 0
#     for numero in numeros :
#         resultado +=numero
#     print( "el resultado de tu super suma es :  \n ", resultado)    


# suma(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)



# def saludar(*nombres):
#     for nombre in nombres:
#         print(f"hola {nombre}")

# saludar("Juan", "Ana", "Pedro")
#***********************************************************************
#       [TAREA]
# Crear función que reciba un día y múltiples nombres (*args)
# Mostrar:
# Día X
# inscrito 1: nombre
# inscrito 2: nombre
# ...
# Usar for para recorrer los nombres
# (opcional) intentar con range(len()) antes de mejorar

# def inscrit (dia, *nombres):
#     print(f" para el dia {dia} \n" + "tenemos los siguientes inscritos:")
#     contador = 0
#     for nombre in nombres :
#             contador+=1  
#             print(contador,nombre)



# inscrit(3,"juan", "maria", "Paco", "Meli")  
#*****************************************************************
# [TAREA]
# Crea una función que:

# reciba datos con **kwargs
# imprima:
# nombre del producto
# precio
# stock
# y además:
# si no viene alguno de esos datos → imprimir "dato no disponible"

#dato
# Reglas:
# usar kwargs como diccionario
# acceder por clave ([...])
# manejar el caso cuando no exista la clave

#*****************************************************************


def get_datos (**datos):
    print(nombre=["name"],nombre=["name"],nombre=["name"],info)