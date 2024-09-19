

a = lambda x: x**2
print(a(10)) # 100

b = lambda y, u: y+u
print(b(2,3)) # 5

x = lambda e: e
print(x(9)) # 9

def spam2(a):
    print(a+6)
spam2(3) # 9

def spam2(a, b):
    print(a+b)
spam2(3, 5) # 8

def spam2(a, b, c=7):
    print(a+b+c)
spam2(3,5) # 15

def test(a, b):
    return a + b
print(test(5, 9)) # 14

all_products = {'Склад': {'name': 'Хлеб', 'количество': 34}}
def get_products(a):
    print(all_products['Склад'][a])
get_products('name') # Хлеб

def test(a, b, y):
    return a * b / y
print(test(10, 25, 3)) # 83.33333333333333

def test(a, b, y, x):
    return a * b / y * x
print(test(245, 567, 10, 50)) # 694575.0

all_products = {'Склад': {'name': 'Хлеб', 'количество': 34}}
def get_products(a = 'name'):
    print(all_products['Склад'][a])
get_products() # Хлеб

def spammer(*args):
    for a in args:
        print(a)
spammer(1,2,3,1,2,3, '4', 'Hello') #

def my1(*args):
    if 'Jordan' in args:
        print('Есть')
    else:
        print('Нету')
my1('Jordan', 'Pasha', 'Pavel') # Есть

def spam1(**kwargs):
    for k,v in kwargs.items():
        print(k,v)
print(spam1(name= 'my1', age= 23)) # name my1  age 23

clients = {}
opened_rooms = [i for i in range(1, 41)]
closed_rooms = []


# Добавление клиента
def add_client(name, room):
    clients[name] = room
    opened_rooms.remove(room)
    closed_rooms.append(room)

# Выселение клиента
def del_client(name):
    closed_rooms.remove(clients[name])
    opened_rooms.insert(clients[name] - 1, clients[name])
    clients.pop(name)

# Список занятых номеров
def show_rooms():
    return closed_rooms


while True:
    choice = input('Введите действие: ')

    if choice.lower() == 'добавить':
        cl_name = input('Имя клиента: ')
        print(opened_rooms)
        cl_room = int(input('Выберите номер: '))
        add_client(cl_name, cl_room)
        print(clients)
    elif choice.lower() == 'выселить':
        cl_name = input('Имя клиента: ')
        if cl_name in clients:
            del_client(cl_name)
            print(clients)
        else:
            print('Такого клиента нет!')
    elif choice.lower() == 'номера':
        print(show_rooms())
    else:
        print('Error')

#  Напишите анонимную функцию, которая принимает два аргумента (числа) и возвращает их сумму.
from random import choice
from tkinter.font import names

b = lambda y, u: y*u
print(b(5,3)) # 15


#Затем напишите программу, которая запрашивает у пользователя два числа и использует анонимную функцию для вычисления и вывода их суммы.
def spam2(a=5, b=8):
    print(a*b)
spam2(5 * 8) # 320

