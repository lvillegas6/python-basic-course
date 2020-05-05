# Un set es una colección desordenada que no tiene un indice
colors = {'Red', 'Green', 'Blue'}
print(type(colors))
print(dir(colors))

print('Red' in colors)

# Agregar un elemento. Lo coloca al inicio.
colors.add('Violet')
print(colors)

# Para eliminar un elemento
colors.remove('Red')
print(colors)

# Limpiar todos los elementos de la colección
colors.clear()
print(colors)

# Del utilizada para eliminar objetos creados, también se puede usar para eliminar variables, listas o partes de una lista, etc.
del colors

# print(colors) Output: Error.