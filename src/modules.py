# own modules
import myMath # me trae todas las funciones o variables que esten en ese archivo
print(myMath.PI)
myMath.add(1, 2)
myMath.substract(2, 1)

 # otra forma de importar. Traemos los metodos directamente
 # sin la necesidad de especificar 
from myMath import add, substract, PI
print(PI)
add(1, 2)
substract(2, 1)

# python modules
import datetime
print(datetime.date.today())
print(datetime.timedelta(minutes=70))

 # otra forma de importar. Traemos los metodos directamente
 # sin la necesidad de especificar 
from datetime import timedelta, date
print(date.today())
print(timedelta(minutes=80))


# thirdy party modules
# 1. install python3-pip and python-php with apt
# 2. install colorama using pip install colorama
from colorama import Fore, Style 

print(Fore.RED + 'Hello world')