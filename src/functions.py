
# Para que sea un funcion debe tener
# la palabra clave 'def' y los parentesis '()'
def sayHello():
    print('Hello')

# Ejecutar la funcion
sayHello()

# parametros
def sayGreeting(name):
    print(f'Hello {name}')

sayGreeting('Luis')
sayGreeting('Ana')

# Argumentos por defectos
def sayGreetingDefault(name='Person'):
    print(f'Hello {name}')

sayGreetingDefault()

# Retornar un valor
def sum(numberOne, numberTwo):
    return numberOne + numberTwo

total = sum(10, 30)
print(total)

# lambda

sum2 = lambda numberOne, numberTwo: numberOne + numberTwo

total2 = sum2(10, 30)
print(total2)