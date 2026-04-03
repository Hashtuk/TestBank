class Dog:
    species = 'Собака'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f'{self.name} лает: Гав!')

dog1 = Dog('Samoyed', 3)
dog2 = Dog('Golden Retriever', 5)
print(f'{dog1.name} это {dog1.species} и ей {dog1.age} лет')
dog1.bark()
print(f'{dog2.name} это {dog2.species} и ей {dog2.age} лет')
dog2.bark()
