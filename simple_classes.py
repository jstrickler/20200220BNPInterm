#!/usr/bin/env python

cities = ['New York', 'Rye', 'Westchester', 'White Plains']
print(type(cities))
cities.append("Albany")

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print("woof! woof!")

s1 = Dog("Fido")
s1.bark()   # Spam.bark(s1)

s2 = Dog("Rin-tin-tin")
s2.bark()

print(s1.name, s2.name)

d = Dog("Fido")
#  Dog d = new Dog("Fido");
