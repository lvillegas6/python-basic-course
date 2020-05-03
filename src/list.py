lista = [1, 'hello', 1.34, True, [1, 2, 3]]
numberList = list([1, 2, 3, 4]) # Creando lista, utilizando el constructor.

colores = ['green', 'red', 'blue']

print(dir(lista))
print(lista)
print(numberList)

print(lista[2])

# list.count(value)
print(colores.count('green'))

# Crear una lista con un rango.
l = list(range(1, 10))
print(l)

# Para saber si un elemento esta en una lista, podemos utilizar el operador "in"
print('hello' in lista)
print('bye' in lista)

# Para agregar un nuevo elemento a la lista.
lista.append('bye')
print(lista)

# Para agregar varios elementos a la misma lista.
# Esto no hace una lista dentro de otra.
lista.extend(['green', 'car'])
print(lista)

# Insertar un elemento, con una posicion establecida.
lista.insert(2, 'world')
print(lista)

# list.pop(index) Quitar el ultimo elemento de la lista y me retorna el valor eliminado.
item = lista.pop()
print(lista)
print(item)

# list.remove(value) Para quitar un item en especifico.
lista.remove('green')
print(lista)

# Para ordenar elementos, alfabéticamente  
colores.sort()
print(colores)

# Para ordenar de forma inversa
colores.sort(reverse=True)
print(colores)

# lista.index(value) Para ver el indice de un elemento:
print(colores.index('blue'))

# Para limpiar toda la lista.
lista.clear()
print(lista)