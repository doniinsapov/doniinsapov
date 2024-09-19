class Animal:
    def __init__(self, breed, name, age):
        self.breed = breed
        self.name = name
        self.age = age

Dog = Animal(breed='Labrador', name='Lyusi', age=5)
print(vars(Dog))

class Animal:
    def __init__(self, breed, name, age):
        self.breed = breed
        self.name = name
        self.age = age

    def sit(self):
        print('Собака села')

    def bark(self):
        print('Собака залаела')

Dog = Animal('Lablador', 'Lyusi', 5)
Dog.sit()#  Дал команду собаке и она села
Dog.bark() # Потом дал команду и она залаела



class Person:
    def __init__(self, name, age, profession):
        self.name = name
        self.age = age
        self.profession = profession

guests1 = Person('Pave', 35, 'driver')
guests2 = Person('Dasha', 25, 'hairdresser')
guests3 = Person('Doni', 39, 'operator')
print(vars(guests1))
print(vars(guests2))
print(vars(guests3))



class Student:

    def __init__(self, name='Ivan', age=18, groupNumber='G-10A'):
        self.name = name
        self.age = age
        self.groupNumber = groupNumber

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getGroupNumber(self):
        return self.groupNumber

    def setNameAge(self, name, age):
        self.name = name
        self.age = age

    def setGroupNumber(self, groupNumber):
        self.groupNumber = groupNumber

    def printStudentInfo(self):
        print(f'Студент: {self.name}\nВозраст: {self.age}\nНомер группы: {self.groupNumber}\n')


def printStudentsInfo(*students):
    for student in students:
        student.printStudentInfo()


student1 = Student('Aleksey', 20, 'G-4B')
student2 = Student('Dasha', 18, 'G-1V')
student3 = Student('Evgeniy', 19, 'G-2J')
student4 = Student('Rigina', 21, 'G-3V')
student5 = Student('Doni', 23, 'G-5D')

student1.setNameAge('Shuhrat', 24)
student2.setGroupNumber('G-4C')

printStudentsInfo(student1, student2, student3, student4, student5)


class Car:
    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year

Sedan = Car(model='CHAZOR', color='white pearl', year=2024)
print(vars(Sedan))

class Car:
    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year

    def start(self):
        print('Машина завелась')

    def stop(self):
        print('Машина заглушилась')

Sedan = Car('CHAZOR', 'white pearl', 2024)
Sedan.start()
Sedan.stop()


class Math:

   def __init__(self, a, b):
       self.a = a
       self.b = b

   def addition(self):
       result = self.a + self.b
       print("Сложение:", result)

   def multiplication(self):
       result = self.a * self.b
       print("Умножение:", result)

   def division(self):
       if self.b != 0:
           result = self.a / self.b
           print("Деление:", result)

       else:
           print("Деление на ноль невозможно.")

   def subtraction(self):
       result = self.a - self.b
       print("Вычитание:", result)

a = float(input("Введите A: "))
b = float(input("Введите B: "))

math_obj = Math(a, b)
math_obj.addition()
math_obj.multiplication()
math_obj.division()
math_obj.subtraction()





















