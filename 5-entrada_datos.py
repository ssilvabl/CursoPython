# Entrada de datos por teclado

# Captura los datos por teclado y se reanuda el programa cuando se le da enter
# La función input() devuelve un valor string
nombre = input("Ingresa tu nombre: ")
# Para converir una entrada de datos en tipo de dato entero se pone antes la función int()
# Para converir una entrada de datos en tipo de dato decimal se pone antes la función float()
edad = float(input("Ingresa tu edad: "))

print(f"Tu nombre es {nombre} y tu edad es {edad}")

print(type(nombre))
print(type(edad))

