class Animal:

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

class Dog(Animal):
    def __init__(self, name, age, breed, color):
        super().__init__(name, age, breed)
        self.color = color

    def bark(self):
        print(f'{self .name} лает')

class Cat(Animal):
    def __init__(self, name, age, breed, color):
        super().__init__(name, age, breed)
        self.color = color

    def purr(self):
        print(f'{self .name} мурлычит')

class Cow(Animal):
    def __init__(self, name, age, bread, color):
        super().__init__(name, age,bread)
        self.color = color

    def moos(self):
        print(f'{self .name} мууу')


dog = Dog('Lyusi', 5, 'Labrador', 'Golden')
cat = Cat('Bakcsa', 8, 'no breed', 'black and white')
cow = Cow('Mashka', 10, 'Golan', 'black and white')

print(f"Dog's name: {dog. name}, age: {dog.age}, breed: {dog.breed}, color: {dog.color}")
print(f"Cat's name: {cat. name}, age: {cat.age}, breed: {cat.breed}, color: {cat.color}")
print(f"Cow's name: {cow. name}, age: {cow.age}, breed: {cow.breed}, color: {cow.color}")

dog.bark()
cat.purr()
cow.moos()

















