product = {
    'name': 'Book',
    'quantity': 3,
    'price': 5
}
print(product) 
print(type(product))
print(dir(product))

# Para obtener las 'key' del diccionario
print(product.keys())

# Para obtener un arreglo de 'key' y 'values'
print(product.items()) # Output: [('name', 'Book'), ('quantity', 3), ('price', 5)]

# Para limpiar o eliminar sus elementos internos
product.clear()
print(product)

# Del utilizada para eliminar objetos creados, también se puede usar para eliminar variables, listas o partes de una lista, etc.
del product

# Podemos agrupar estos diccionarios en una lista como en JavaScript
products = [
    {'name': 'book'},
    {'name': 'laptop'}
]
print(products)