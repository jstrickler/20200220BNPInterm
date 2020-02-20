#!/usr/bin/env python
from carddeck import CardDeck
from jokerdeck import JokerDeck

d1 = CardDeck("Fred")
d2 = CardDeck("Euphonia")

print(d1)
print(d2)

print(d1.dealer)

d1.dealer = "Maria"
# CardDeck.dealer(d1, "Maria")
print(d1.dealer)

try:
    d1.dealer = 123.4
except TypeError as err:
    print(err)

print(dir(d1))

d1.shuffle()
print(d1.cards)

for i in range(5):
    print(d1.draw())
print()

j1 = JokerDeck("Abby")
print(j1)
j1.shuffle()
print(j1.cards)


print(len(d1))
print(d1)
print(j1)

x = d1 + j1
print(x)
print(len(x))



