name = 'Javlon'
favourite_number = 7
value_of_pi = 3.14
print(name)            #Javlon
print(favourite_number) #7
print(value_of_pi)  #3.14

name, age = 'Pavel', 21
print(name,age) # Pavel 21

name = 'Pavel'
name = 'Slavik'
print(name)  #Slavik

name=age=spam= 'Chto eto???'
print(name,age,spam)   # Chto eto??? Chto eto??? Chto eto???

spam,spam1 = 36, 40
print(spam,spam1) # 36, 40

spam,spam1 = 36, 40
print(type(spam)) #<class 'int'>

spam = 2.00
print(type(2.00)) #<class 'float'>

Python = 'Privet mir'
print(Python) # Privet mir

string = '2'
print(type('2'))

text = 'Hello world!'
number = 79
decimal_number = 5.0
print(text)  # Hello world!
print(number) # 79
print(decimal_number) # 5.0

integer = 3 + 6 ** 2
print(3 + 6 ** 2) # 39
print(7 * 3 ** 2)  #63
print(7 // 2 + 0.5) #3,5
print(3 % 2 * 2) # 2

x = 7
y = 'eto chislo'
print(x,y) # 7 eto chislo

x = 'mikro'
y = 'fon'
print(x+y) #mikrofon

x = 20
y = 99
print(x+y) #119

x = 7
y = 'Kak dela'
print(x*y) #Kak delaKak dela...

x = 7
y = 5.6
print(x*y)

str = 'hello world'
int = 2
print(str*int) #hello worl dhello world

srok = 2
print('YA stal specialistom za {} mesyaca'.format(srok))
#YA stal specialistom za 2 mesyaca
print(f'YA stal specialistom za {srok} mesyaca')
# YA stal specialistom za 2 mesyaca
print('YA stal specialistom za %d mesyaca' %(srok))
# YA stal specialistom za 2 mesyaca

player1 = input('Введите действие, игрок1: ')
player2 = input('Введите действие, игрок2: ')
if player1 == 'Ножницы' and player2 == 'Бумага':
    print('Игрок1 выиграл!')
elif player1 == 'Ножницы' and player2 == 'Камень':
    print('Игрок2 выиграл!')


