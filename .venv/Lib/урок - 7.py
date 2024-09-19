def say_hello():
    print('Hello World')
say_hello() # Hello World

def create_iist():
    my_list = []
    print(my_list)
create_iist() # []

def f(x):
    return 2 * x + 3
print(f(3)) # 9

def create_list():
    my_list =[]
    return my_list
a = create_list()
a.append(5)
print(5) # 5

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



