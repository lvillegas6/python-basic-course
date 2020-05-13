# es como tener una funcion dentro de otra func = add(sum(1,2))
# algo parecido a lo que se usa como un callback
def subtractOne(f):
    def sum(a, b):
        print(f'Valor {f(a,b)}')
        total = f(a,b)
        return total - 1
    return sum

@subtractOne
def sum(a,b):
    return a + b


def subtractOne2():
    def decorator(f):
        def sum(a, b):
            print(f'Valor {f(a,b)}')
            total = f(a,b)
            return total - 1
        return sum
    return decorator

@subtractOne2()
def sum2(a,b):
    return a + b



print(sum(1, 2))
print(sum2(1,2))
