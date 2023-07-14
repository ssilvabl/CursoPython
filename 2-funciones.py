# FUNCIONES


"""
Uso de función sin parámetros: def nombreFuncion():
    Instrucciones
Uso de función con parámetros: def nombreFuncion(param1, param2):
    instrucciones

Llamar a la función sin parámetros: nombreFuncion()
Llmar a la función con parámetros: nombreFuncion(param1, param2)

El return sirve para devolver el resultado de la función

"""

# Función mostrar texto
def mostrarTexto():
    print("Buenos días")

# Ejecutar Función
mostrarTexto()

# Función con parámetro mostrar texto
def mostrarTexto2(texto):
    print(texto)

nombre = "santiago"

# Ejecutar función
mostrarTexto2(nombre)

# Función con return
def mostrarTexto3(texto):
    return texto

# Llamar y mostrar resultado de la función
print(mostrarTexto3(nombre))


