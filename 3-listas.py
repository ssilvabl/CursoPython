# LISTAS


# Uso: nombreLista = [elemento1, elemento2, etc]

# Lista de nombres
listaNombres = ["santiago", "valentina", "juan", "maria", "pedro"]
# Imprimir todos los elementos de la lista
#print(listaNombres[:])

# Imprimir un índice en particular
#print(listaNombres[2])

# Imprimir en un rango (num1:donde comienza el rango : num2:donde termina el rango y excluye el índice indicado)
""" print(listaNombres[0:2])
print(listaNombres[:2])
print(listaNombres[1:2])
print(listaNombres[1:]) """

# Función para agregar elemento a una lista
# Uso: nombreLista.append(elementoAAñadir) -> se agrega al final de la lista
# Uso: nombreLista.insert(indice del lugar al que se va a añadir, elementoAAñadir) -> se agrega en una posición en específico
# Uso: nombreLista.extend([elemento, elemento2]) -> Agregar múltiples elementos o agregar una lista completa

# Aladir elemento a la lista
listaNombres.append(1999)
#print(listaNombres[:])

listaNombres.insert(2, "laura")
#print(listaNombres)

listaNombres.extend(["santi", "miguel", 21])
#print(listaNombres)

# Buscar indice utilizando el elemento (sólo devuelve el indice del primer elemento que coincida)
# Uso: listaNombres.index("santi") -> devuelve el indice en el que está el elemento "santi"

#print(listaNombres.index("valentina"))

# Validar si un elemento existe en una lista
# Uso: print("elementoABuscar" in listaNombres) -> devuelve True o False

statusValidate = "santi" in listaNombres
#print(statusValidate)

# Remover elementos de la lista
# Uso: listaNombres.remove(elementoAEliminar)
# Uso: listaNombres.pop() -> Elimina el último elemento de la lista y lo puede almacenar
# Uso: del listaNombres[indice_eliminar] -> Elimina el elemento que pertenece a ese índice
# Uso: listaNombres.clear() -> Elimina todos los elementos de una lista

listaNombres.remove("santiago")
#print(listaNombres)

# Unir listas
listaNombres2 = ["ana", "maria", "sefue"]
listaNombres3 = listaNombres + listaNombres2
#print(listaNombres3)

# Multiplicar listas
listaNombres4 = ["ana", "maria", "sefue"] * 4
#print(listaNombres4)

mi_lista = ["santiago", "valentina", "monica", "pedro", "juan", "guillermo"]
print(mi_lista)
"""
# Modificar elemento teniendo el índice
mi_lista[0] = "Juan"
print(mi_lista)

# Crear una sublista a partir de una lista
# Primero se indica el índice donde empezará y segundo el índice donde terminará (se excluye el índice que indica)
sub_lista = mi_lista[0:3]
print(sub_lista)

# Crear sublista a partir de un índice en particular
sub_lista2 = mi_lista[1:3]
print(sub_lista2)

# Crear sublista desde el primer elemento hasta un índice n
sub_lista3 = mi_lista[0:3]
print(sub_lista3)

# Acceder al último elemento
print(mi_lista[-1])

# Acceder desde un índice n hasta el último elemento
print(mi_lista[2:])
"""

# Generar salto de elementos(se indica en el último parámetro el número en el que realizará cada salto)
print(mi_lista[0:-1:2]) # Para inverti el salto de los elementos, sólo se debe poner el -1

# Obtener la longitud(cantidad de elementos) de una lista
print(len(mi_lista))

# Ordenar lista de elementos (por default en forma ascendente)
mi_lista.sort()
# Ordenar de forma descendente
mi_lista.sort(reverse=True)
print(mi_lista)

# Obtener el número menor de una lista
mi_lista_num = [3, 5, 66, 656, 2, 23, 90, 0, 5]
print(min(mi_lista_num))
# Obtener el número mayor
print(max(mi_lista_num))

# Validar si un elemento existe en una lista
print(5 in mi_lista_num)
# Validar si un elemento no existe en una lista
print(5 not in mi_lista_num)

# Obtener el índice de un elemento (sólo devuelve el índice del primer elemento encontrado)
index = mi_lista_num.index(5)
print(index)