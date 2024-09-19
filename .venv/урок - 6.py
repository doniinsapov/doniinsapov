from dbm import error
from itertools import product
from tkinter.font import names

x = {'name': 'Pasha', 'Job': 'TgBot creator'}
print(x['name']) # Pasha

x = {'name': 'Pasha', 'Job': 'TgBot creator'}
print(x['Job']) # TgBot creator

data = {'name': 'Jordan', 'age': 12, 'job': 'python programmer'}
print(data['name'],data['job']) # Jordan python programmer

data = {'name': ['jordan', 'Pavel'], 'age': (12, 21), 'job': 'programmer'}
print(data['name'][0], data['job'][-1]) # jordan r

instructor = {'name': 'Jordan', 'age': 21, 'job': 'programmer'}
#.values() выдаст все значения ключей
print(instructor.values()) # dict_values(['Jordan', 21, 'programmer'])

instructor = {'name': 'Jordan', 'age': 21, 'job': 'programmer'}
# .keys() выдаст все ключи словаря
print(instructor.keys()) # dict_keys(['name', 'age', 'job'])

instructor = {'name': 'Jordan', 'age': 21, 'job': 'programmer'}
# .items() выдаст оба (ключ и значения) словаря
print(instructor.items()) #dict_items([('name', 'Jordan'), ('age', 21), ('job', 'programmer')])

users = {} # пустой словарь
users['name'] = 'Jordan' # добавляет ключ 'name' в пустой
                         # словарь users со значением 'Jordan'
print(users) # {'name': 'Jordan'}
print(users['name']) # Jordan

song = {'name': 'Godzilla', 'singer': 'Eminem'}
song['genre'] = 'Hip-Hop'
print(song) # {'name': 'Godzilla', 'singer': 'Eminem', 'genre': 'Hip-Hop'}
# этот пример добавил ключ и значение

cafees = {'Evos':{'Gorod': 'Tashkent', 'Filialov': 'mnogo', 'Okritie': 2007}}
cafees['Evos']['кухня'] = 'Fast Food'
print(cafees) # {'Evos': {'Gorod': 'Tashkent', 'Filialov': 'mnogo', 'Okritie': 2007, 'кухня': 'Fast Food'}}

songs = {}
songs['Singer'] = 'Eminem'
songs['name'] = 'Godzilla'
print(song) # 'name': 'Godzilla', 'singer': 'Eminem',

my_dict = {'name': 'Jordan'}
my_dict['name'] = 'Pasha'
print(my_dict) # поменял значение  Jordan na Pashu

my_dict = {'name': 'Jordan'}
my_dict['name'] = ['Jordan']
my_dict['name'].append('Pavel')
print(my_dict) #{'name': ['Jordan', 'Pavel']} добавил значение в список

my_dict = {'song': 'Godzilla', 'singer': 'Eminem'}
my_dict.clear() # удаляет всё
print(my_dict) # {}

my_dict = {'song': 'Godzilla', 'singer': 'Eminem'}
my_dict.pop('song') # удаляет пару из словаря по переданному ключу
print(my_dict) # {'singer': 'Eminem'}

my_dict = {'song': 'Godzilla', 'singer': 'Eminem'}
my_dict.popitem() # удаляет последнюю пару (ключ и значения)
print(my_dict) # {'song': 'Godzilla'}

{}.fromkeys('a', 1)
print({}.fromkeys('song', 'Godzilla'))
#{'s': 'Godzilla', 'o': 'Godzilla', 'n': 'Godzilla', 'g': 'Godzilla'}

my2 = {'title': 'Python for beginners'}
# .get() выдаёт значение переданного ключа
print(my2.get('title')) # Python for beginners

my_dict = {'name': 'Jordan'}
my_dict.clear()
print(my_dict)

my = dict(name='Jordan', job='Developer', age=23)
my2 = my.copy()
print(my2) # {'name': 'Jordan', 'job': 'Developer', 'age': 23}

my = dict(name='Jordan', job='Developer', age=23)
my2 = my.get('name')
print(my2) # Jordan

nums = {1, 2, 3, 4, 4, 5, 6, 7, 7}
print(nums) #{1, 2, 3, 4, 5, 6, 7}

names = (11, 22, 22, 333, 333, 3)
names2 = set(names)
print(names2) # {3, 11, 333, 22}

names = ['Pavel', 'Pavel', 1, 1, 2, 2]
names2 = set(names)
print(names2) # {1, 2, 'Pavel'}

my = ['2', '33', '33', 2, 'TgBot']
my2 = set(my)
print(my2) # {'2', 2, 'TgBot', '33'}

instructor = dict(name='Jordan', age=32, job='Python developer')
for v in instructor.keys(): # выдаёт все ключи
    print(v) # name age gob

instructor = dict(name='Jordan', age=32, job='Python developer')
for v in instructor.values(): # выдаёт все значения
    print(v) # Jordan 32 Python developer

instructor = dict(name='Jordan', age=32, job='Python developer')
for k, v in instructor.items(): # выдаёт ключ и значения
    print(k,v) # name Jordan age 32 job Python developer

all_products = {'Ввесь склад': {}}
korzina = []
while True:
    admin = input('ВЫберите действие: ')
    if admin.upper() == 'ДОБАВИТЬ':
        products_name = input('Введите название товара: ')
        products_count = int(input('Введите количество товара: '))
        all_products['Ввесь склад'][products_name] = products_count
        print('Товар добавлен!')
    elif admin.upper() == 'ТОВАР':
        print(all_products)
    elif admin.upper() == 'КУПИТЬ':
        print(all_products)
        # Выбор товара для ПОКУПКИ
        pr_name = input('Выберите покупки: ')
        # выбор количества товара для ПОКУПКИ
        pr_count = int(input('Выберите количество товара: '))
        # Проверка есть ли товар на складе и его количество первышает то, которое покупает пользователь
        if pr_name in all_products['Ввесь склад'] and all_products['Ввесь склад'][pr_name] >= pr_count:
         # Собераем заказ
         new_order = (pr_name, pr_count)
         # Добавляем в корзину
         korzina.append(new_order)
         # Минусуем товар со склада
         all_products['Ввесь склад'][pr_name] -= pr_count
         print('Товар успешно помещён в корзину! ')
    else:
        print('Error')









