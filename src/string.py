texto = 'Hello world'

# Nos muestra todo lo que podemos hacer con este tipo de datos.
# dir(texto)
print(dir(texto))

print(texto.upper())
print(texto.lower())
print(texto.swapcase())
print(texto.capitalize())
print(texto.replace('Hello', 'bye'))
print(texto.count('l')) # output 3 porque la "l" sale 3 veces en el texto.
print(texto.startswith('Hello'))
print(texto.endswith('world'))

print(texto.split()) # === print(texto.split(' '))
print(texto.find('o')) # return la posicion donde encontro el caracter

# len(text)  length
print(len(texto))

# Index: Retorna la posicion del caracter.
print(texto.index('e'))

print(texto.isnumeric())
print(texto.isalpha())

print(texto[4])
print(texto[-1]) # Comienza a lo contrario.

name = 'Luis'
print('My name is ', name)
print('My name is ' + name)
print(f'My name is {name}')