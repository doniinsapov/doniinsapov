numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in numbers:
    print(i * 2) # 2 4 6 8 10 12 14 16 18 20

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in numbers:
    print(i / 2) # 0.5, 1.0, 1.5, 2, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
half_numbers = []
for i in numbers:
    half_numbers.append(i / 2)
print(half_numbers) # [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]

names = ['Ivan', 'Pavel', 'Aleksandr']
for i in names:
    print(f'Здраствуйте, уважаемый {i}! Рады пригласить вас на замечательное'
          f'событие Mocfest! Ждём вас с 18:00 до 23:00! ')
    #Здраствуйте, уважаемый Ivan! Рады пригласить вас на замечательноесобытие Mocfest! Ждём вас с 18:00 до 23:00!
    #Здраствуйте, уважаемый Pavel! Рады пригласить вас на замечательноесобытие Mocfest! Ждём вас с 18:00 до 23:00!
 #Здраствуйте, уважаемый Aleksandr! Рады пригласить вас на замечательноесобытие Mocfest! Ждём вас с 18:00 до 23:00!

names = ['Ivan', 'Pavel', 'Aleksandr']
num = 1
for i in names:
    print(f'{num}) Здраствуйте, уважаемый {i}! Рады пригласить вас на замечательное'
          f'событие Mocfest! Ждём вас с 18:00 до 23:00! ')
    num = num + 1
#  1) Здраствуйте, уважаемый Ivan! Рады пригласить вас на замечательноесобытие Mocfest! Ждём вас с 18:00 до 23:00!
# 2) Здраствуйте, уважаемый Pavel! Рады пригласить вас на замечательноесобытие Mocfest! Ждём вас с 18:00 до 23:00!
# 3) Здраствуйте, уважаемый Aleksandr! Рады пригласить вас на замечательноесобытие Mocfest! Ждём вас с 18:00 до 23:00!

my_list = (6, 'a', '2')
for p in my_list:
    print(p)
print(f'Всего {len(my_list)} элемента(ов)') # 6, a, 2 всего три элемента

my_list = (6, 4)
for t in my_list:
    print(t+2) # 8, 6,

for i in range(100):
    print('Hello world! ') # сто раз 'Hello world!

my_tuple = (6, 4, '2')
for i in range(1, 100):
    print(f'{my_tuple}') # (6, 4, '2') - 99 raz

for i in range(100):
    print(i)

for i in range(1, 100, 2):
    print(i)

names = ['Ivan', 'Pavel', 'Jordan', 5]
for i in range(1, 20):
    if 'Pavel' in names:
        print('Pavel есть в списке')
    else:
        print('Не понимаю о ком вы') # Pavel есть в списке (19 раз)

words = ['abort', 'bake', 'beam', 'confide', 'grill', 'wave']
past_tense = []
for word in words:
    if word[-1] == 'e':
        past_tense.append(word+'ed')
    else:
        past_tense.append(word+'d')
print(past_tense) # ['abortd', 'bakeed', 'beamd', 'confideed', 'grilld', 'waveed']

p = ['m', 'my', 23]
i = 0
while i < len(p):
    print(p[i])
    i = i + 1 # m, my, 23

print("doni")
print("doni@gmail.com") #doni doni@gmail.com

acre = 43560
foots_long = int(input('Введите длину в футах: '))
foots_width = int(input('Введите ширину в футах: '))
result = (foots_long * foots_width) / acre
print(f'{result} акров')

