"""Los operadores lógicos evalúan una expresión y devuelven un valor
falso o verdadero, y esto son:

and (se deben cumplir ambas condiciones para ser True)
or (se debe cumplir al menos una condición para ser True)
not (niega la expresión, es decir, si es True lo vuelve False)"""

numero_uno = 5
numero_dos = 24

# and (y)
resultado = (numero_uno and numero_dos) >= 100
print(resultado)

# or (o)
resultado = (numero_uno or numero_dos) >= 100
print(resultado)

# not (negar)
resultado = not (numero_uno and numero_dos) >= 100
print(resultado)
