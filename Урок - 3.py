names = ['Ivan', 'Pavel', 'Jordan', 5]
print(type(names)) # <class 'list'>

names = [1, 2, 3, 4, ['Hello', 3, '5']]
print(type(names)) #<class 'list'>

names = [1, 2, 3, 4, ['Hello', 3, '5']]
print(len(names)) # 5

names = ['Ivan', 'Pavel', 'Jordan', 5]
print(len(names)) # 4
print(names[2]) # Jordan

p = [1, 2, 'Python', 'TgBot']
print(p[3]) # TgBot

p = [1, 2, 'Python', 'TgBot']
print(p[-1]) # TgBot

names = ['Ivan', 'Pavel', 'Jordan']
print(names[-2]) # Pavel
print(names[1][2]) # v

names = ['Ivan', 'Pavel', 'Jordan',[5, 4, 3, 2, 1]]
print(names[-1][2]) # 3

names = ['Ivan', 'Pavel', 'Jordan',[5, 4, 3, 2, 1]]
print(names[1]) # Pavel
print(names[-1]) # [5, 4, 3, 2, 1]

names = [1, 2, 3, 4, 'Hello', 3, '5']
print(names[2:4]) # [3, 4] до Hello

toys = ['Мишка','Мячик','Робот','Машинка']
print(toys[2:])  #['Робот','машинка']

toys = ['Мишка','Мячик','Робот','Машинка']
print(toys[0:1]) # [мишка]

toys = ['Мишка','Мячик','Робот','Машинка']
print(toys[:3]) # [Мишка, Мячик, Робот]

names = ['Ivan', 'Pavel', 'Jordan',[5, 4, 3, 2, 1], 5]
print(names[:3]) #['Ivan', 'Pavel', 'Jordan']

names = [1, 2, 3, 4, 'Hello', 3, '5']
print(names[2:4:2]) # [3]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[::2]) # [1, 3, 5, 7, 9] (нечётное)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[1::2]) # [2, 4, 6, 8, 10] (чётное)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[1::3]) # [2, 5, 8]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers.append(11)
numbers.insert(0, 0)
numbers.extend([12, 13, 14, 15])
print(numbers) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

names = ['Sasha']
names.append('Pavel')
print(names) # ['Sasha', 'Pavel']

names = ['Loki', 'Spider-man']
names.insert(0, 'thor')
print(names) #['thor', 'Loki', 'Spider-man']

names = ['Loki', 'Spider-man']
names.extend(['Thor', 0, 23, 'Tanos'])
print(names) # ['Loki', 'Spider-man', 'Thor', 0, 23, 'Tanos']

names = ['Loki', 'Thor', 'Hulk']
names.clear()
print(names) # []

names = ['Loki', 'Thor', 'Hulk']
names.pop()
print(names) #['Loki', 'Thor']

names = ['Loki', 'Thor', 'Hulk']
names.pop(0)
print(names) # ['Thor', 'Hulk']

names = ['Loki', 'Thor', 'Hulk']
names.remove('Loki')
print(names) # ['Thor', 'Hulk']

names = ['Pavel', 'Python', 'TgBot', 'Django']
#names [индекс элемента который хотим изменить]
names[0] = 'Tehnikum'
print(names) #['Tehnikum', 'Python', 'TgBot', 'Django']

names = ['Pavel', 'Kane', 'Aleks', 'Dima']
names.sort()
print(names) #['Aleks', 'Dima', 'Kane', 'Pavel']

names = ['Pavel', 'Kane', 'Aleks', 'Dima']
names.reverse()
print(names) #['Dima', 'Aleks', 'Kane', 'Pavel']

names = ['Pavel', 'Python', 'TgBot', 'Django']
# список.index(значение)
names_index = names.index('Pavel')
print(names_index) # 0 (т.к 'Pavel' находится под 0 индексом)

names = ['Loki', 'Thor', 'Hulk']
names[2] = 'Spider-man'
print(names) # ['Loki', 'Thor', 'Spider-man']

names = 'Ivan', 'Pavel', 'Jordan', 5
print(names) # ('Ivan', 'Pavel', 'Jordan', 5)

names = (1, 2, 3, 4, ['Hello', 3, '5'])
print(len(names)) # 5 ( len Узнаёт сколько элементов)

names = ('Ivan', 'Pavel', 'Jordan')
print(len(names)) # 3
print(names[2]) # Jordan

my = (1, 2, 'Python', 'TgBot')
print(my[3]) # TgBot

my = (1, 2, 'Python', 'TgBot')
print(my[-1]) # TgBot

names = ('Ivan', 'Pavel', 'Jordan')
print(names[-2]) # Pavel
print(names[2][3]) # D

names = (1, 2, 3, 4, 'Hello', 3, '5')
print(names[3:]) # (4, 'Hello', 3, '5')

toys =('Мишка', 'Мячик', 'Робот', 'Машинка')
print(toys[1:]) #('Мячик', 'Робот', 'Машинка')

toys =('Мишка', 'Мячик', 'Робот', 'Машинка')
print(toys[0:3]) # ('Мишка', 'Мячик', 'Робот')

toys =('Мишка', 'Мячик', 'Робот', 'Машинка')
print(toys[1::2]) # ('Мячик', 'Машинка')

names = (1, 2, 3, 4, 'Hello', 3, '5')
print(names[2:4:2]) # (3,)

toys =('Мишка', 'Мячик', 'Робот', 'Машинка')
toys2 = list(toys)
print(toys2) # ['Мишка', 'Мячик', 'Робот', 'Машинка']
print(type(toys)) #<class 'tuple'>

toys =('Мишка', 'Мячик', 'Робот', 'Машинка')
toys2 = tuple(toys)
print(toys2) # ('Мишка', 'Мячик', 'Робот', 'Машинка')
print(type(toys2)) #<class 'tuple'>

lang =['English', 'Python', 'Русский', 4, 45]
if 'English' in lang:
    print('Я знаю английский') # Я знаю английский
elif 'Python' in lang:
    print('Я владею Python')
else:
    print('Повторите пожалуйста')

names = (1, 2, 3, 4, 'Hello', 3, '5')
if 2 in names and 'Hello' in names:
    print(names[2:4:2]) # (3,)

names = (1, 2, 3, 4, 'Hello', 3, '5')
if 2 in names or 'Python' in names:
    print(names[-1]) # 5

names = ['Pavel', 'Jordan', 'Sasha']
new_names = input('Введите новое имя: ')
names.append(new_names)
print(names)
names_to_delete = input('Введите имя для удаления: ')
if names_to_delete in names:
    names.remove(names_to_delete)
    print(names)
else:
    print('Такого имени нет!')
names_to_change = input('Введите имя для изменения: ')
if names_to_change in names:
    change_names = input('Введите изменённное имя: ')
    names[names.index(names_to_change)] = change_names
    print(names)


