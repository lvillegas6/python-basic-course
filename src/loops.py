# FOR
for latter in 'Hello':
    print(latter) 

print('--------')

foods = ['apples', 'bread', 'cheese', 'milk']
# bucle
for food in foods:
    print(food)

print('--------')
# break
for food in foods:
    if food == 'cheese':
        break
    print(food)

print('--------')
# continue
for food in foods:
    if food == 'cheese':
        continue
    print(food)

print('--------')
# Range
for number in range(1,5):
    print(number)

print('--------')
for number in range(5):
    print(number)

print('--------')

# While
count = 1
while count <= 5:
    print(count)
    count += 1