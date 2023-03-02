class Animal:
    def __init__(self, name) -> None:
        self.name = name
    
    def talk(self):
        raise NotImplementedError('Subcalss must implement abstract method')

class Cat(Animal):
    def talk(self):
        return 'Meow!'

class Dog(Animal):
    def talk(self):
        return 'Woof! Woof!'

animals = [Cat('Missy'), Cat('Mr.Mistoffelees'), Dog('Lassie')]
for animal in animals:
    print(animal.name + ': ' + animal.talk())