


students = {}

show_classes = []



# Добавление ученика
def add_student(name, classe):

    students[name] = classe


# удалить ученика
def del_student(name):


    students.pop(name)



# Список классов с учениками
def show_classe():
    return show_classes


while True:
    choice = input('Введите действие: ')

    if choice.lower() == 'добавить':
        st_name = input('Имя ученика: ')
        print(st_name)
        st_classe = input('Выберите класс: ')
        add_student(st_name, st_classe)
        print(students)
    elif choice.lower() == 'удалить':
        st_name = input('Имя ученика: ')
        if st_name in students:
            del_student(st_name)
            print(students)
        else:
            print('Такого ученика нет!')
    elif choice.lower() == 'классы':
        print(students)
    else:
        print('Error')
































