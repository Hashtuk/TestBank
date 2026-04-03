from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.__name = name

    @abstractmethod
    def make_sound(self):
        pass

    @property
    def get_name(self):
        return self.__name


class Lion(Animal):
    def make_sound(self):
        print(f'{self.get_name} рычит: Рррр!')


class Parrot(Animal):
    def make_sound(self):
        print(f'{self.get_name} говорит: Привет!')


class Zoo:
    def __init__(self):
        self.animals: list[Animal] = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def show_all_sounds(self):
        for a in self.animals:
            a.make_sound()


zoo = Zoo()

lion = Lion('Simba')
parrot = Parrot('Kesha')

zoo.add_animal(lion)
zoo.add_animal(parrot)

zoo.show_all_sounds()