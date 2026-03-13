# key works arguments aca se usan dos * ( asterisco)
# la idea es que se usa como dicionario, el nombre y su descripcion por ej


# def get_product(**datos):
#     print(datos["desc"],datos["id"])



# get_product(id="45",
#             name="Iphone",
#             desc="esto es un telefono Iphone")



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


# def get_datos(**datos):
#     if "name" in datos:
#         print("name:", datos["name"])
#     else:
#         print("name: no disponible")

#     if "precio" in datos:
#         print("precio:", datos["precio"])
#     else:
#         print("precio: no disponible")

#     if "stock" in datos:
#         print("stock:", datos["stock"])
#     else:
#         print("stock: no disponible")



# #get_datos(name="celular chino", precio = "1000", stock="25")
# get_datos(altura="1m"); 

# pille a chat en este scrip ESTABA CON ERROR CONCEPTUAL 
# def get_datos(item, **datos):
#     if item in datos:
#         print(f"{item}: {datos[item]}")
#     else:
#         print(f"{item}: no disponible")


# Ejemplos:

#get_datos("name", name="celular chino", precio=1000, stock=25)
#get_datos("precio", name="celular chino", precio=1000, stock=25)



def get_datos(item, **datos):
    
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

    if item not in datos:
        print(f"{item}: no disponible")



get_datos(altura="altura", name="celular chino", precio=1000, stock=25)