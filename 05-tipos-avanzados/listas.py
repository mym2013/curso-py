# Capítulo 5: Tipos Avanzados

# En este capítulo exploramos herramientas 
# más potentes de Python que permiten trabajar
# con datos de forma más estructurada, segura 
# y expresiva. Estos tipos avanzados ayudan
# a escribir código más claro, mantenible y profesional.

# Tipos avanzados (muy breve):

# Tuplas (tuple) → listas inmutables
# Conjuntos (set) → colecciones sin duplicados
# Diccionarios (dict) → pares clave-valor
# Tipos anotados (typing) → pistas de tipo
# Clases (class) → estructuras personalizadas
# Dataclasses → clases simplificadas para datos








numeros = [1,2,3]
letras = ["a","b","c"]
palabras = ["sebi", "boom"]
PalabrasLindas =["amor","respeto","compasión"]

print(numeros)
#******************

booleans =[True, True, False, False, True]
matriz = [[0,1],[1,0]]
print(matriz)

#******************

ceros = [0] + 2*[0]
print(ceros)
alfanumericos = numeros + letras
print(alfanumericos)

rango = list (range(1,11))
print(rango)

name = list ("Gonzalo")
print(name)