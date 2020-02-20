#!/usr/bin/env python

# UI (AKA UX)
def spam():
    print("spam spam spam")

spam()
spam()
spam()

# business logic
def ham():
    return 42

x = ham()
print(x)

def round2(n):
    return round(n, 2)

print(round2(5.93920392))
m = round2(8.239023)
print(m)
x = round2(37)
print(x)

# x = round2()

def double_it(x):
    return x * 2

print(double_it("Pizza1"))
print(double_it(25))
print(double_it(4.7))

def foo(x):
    return 45


print(foo('abc'))



def hello(whom="world"):
    print("Hello", whom)


hello("world")
hello("sailor")
hello()
print()

def greet(greeting, *whom):
    for who in whom:
        print(greeting, who)
    print('---')

greet("Hello", "World")
greet("Hi", "Mom", "Dad")
greet("'sup", "Harry", "Walter", 'Chloe', 'Khadija')



def greetmore(greetings_list, person_list):
    pass


people = ['Paul', 'Dora', 'Mabel', 'T.B.']

greet("HIYA", *people)

def add(x, y):
    return x + y

print(add(5, 10))
print(add(1.2343, 13))

values = [9, 1.2, 4]

print(add(*values[:2]))

greet("hi")

def config(**weaseldust):
    print(weaseldust)
    print()
    for k, v in weaseldust.items():
        print(k, v)

config(animal="wombat", river="Seine", city="Houston")








































