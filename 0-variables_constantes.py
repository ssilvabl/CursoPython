# VARIABLES 


# Los comentarios se pueden establecer con # para una línea o con """ cuando sean multilinea """

# Tipos de variables

# int - enteros
num1 = 12

# float - flotantes
num2 = 2.3

# string - cadena de texto
name = "Santiago"

# bool - booleano
status = True
status = False

""" También se pueden establecer muchas variables
en una misma línea de código, pero se recomienda
que sea 3 máximo 4 y en lo posible del mismo contexto
"""
nombre, apellidos, lugar_nacimiento = "santiago", "silva", "pereira"

# Constante
# Son una varible, pero por convención se escribe todo el nombre mayúscula sostenida
NOMBRE_PROGRAMA = "Variables"

# Imprimir datos en consola
print(nombre, apellidos, lugar_nacimiento)

# Imprimir datos en consola con formato (se agregan las variables entre llaves {nombre_variable})
print(f"{nombre} y {apellidos}")

# Imprimir con saltos de línea
print("""Hola, soy santiago
silva
blandón""")
