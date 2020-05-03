# String
texto = 'Hello Word'
print(texto)

print(type(texto)) # Para ver el tipo de dato.

# Numbers
edad = 10 # Integer
print(edad)
print(type(edad))

temperatura = 15.4 # Float
print(temperatura)
print(type(temperatura))

# Boolean
verdad = True
falso = False
print(type(verdad))

# list
numeros = [10, 20, 10]
palabras = ['Hello', 'World', 'Hi']
combinados = [10, 'Hellow', True, [2, 3]]
print(combinados)
print(type(numeros))

# Tuples 
tuplas = (10, 20, 10, (9, "Julio", 1988)) # Igual a las listas, pero sus elementos no pueden ser modificados.
print(tuplas)
print(type(tuplas))

# Dictorionies | dict
diccionarios = { # 'KEY': VALUE funcionan como los objetos en JS
'nombre': 'Ryan',
'apellido': 'Ray',
}
print(type(diccionarios))

# None
none = None

# Variables en una sola linea

x, book = 100, 'I Robot'
print(x, book)

# Constante
PI = 3.1416