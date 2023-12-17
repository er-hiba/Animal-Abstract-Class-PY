from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @name.setter
    def name(self, name):
        self._name = name

    @age.setter
    def age(self, age):
        self._age = age 

    @property
    def info(self):
        return f"Name: {self._name} and age: {self._age}"

    @abstractmethod
    def sound(self):
        pass

class Horse(Animal):
    def sound(self):
        return "Neighing"

class Cat(Animal):
    def sound(self):
        return "Meowing"

class Dog(Animal):
    def sound(self):
        return "Barking"
