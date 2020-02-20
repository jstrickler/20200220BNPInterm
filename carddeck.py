#!/usr/bin/env python
import random

class CardDeck:
    SUITS = 'C D H S'.split()
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

    def __init__(self, dealer_name):
        self.dealer = dealer_name
        self._build_deck()

    def _build_deck(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = rank, suit  # tuple...
                self._cards.append(card)

    def draw(self):
        return self._cards.pop()

    @property
    def cards(self):
        return self._cards


    def shuffle(self):
        random.shuffle(self._cards)

    @property
    def dealer(self):   # getter property
        return self._dealer_name

    @dealer.setter
    def dealer(self, dealer_name):  # setter property
        if isinstance(dealer_name, str):
            self._dealer_name = dealer_name
        else:
            raise TypeError("Dealer must be a str")


if __name__ == '__main__':

    c = CardDeck("Charles")
    print(c)
