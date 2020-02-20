#!/usr/bin/env python
from abc import ABCMeta, abstractmethod

class AnimalBase(metaclass=ABCMeta):

    @abstractmethod
    def move(self):
        pass

class Dog(AnimalBase):
    def move(self):
        print("moving....")

d = Dog()
d.move()

