

# def sldo(nombre,apellido):
#     print("hello")
#     print(f"que pasa {nombre} {apellido}")

# sldo("Gonzalin", "bombin")
# sldo("angelica", "mama")

#parametros opcionales 
def sldo(nombre,apellido="happy human"): # apellido="happy human, a esto se le llaman, parámtetos opcionales
    print("hello")
    print(f"que pasa {nombre} {apellido}")

sldo("Gonzalin", "bombin")
sldo("angelica")

sldo("Fernando") 
sldo( apellido ="Torres", nombre = "Gonzalo")