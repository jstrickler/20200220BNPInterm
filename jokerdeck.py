#!/usr/bin/env python
from carddeck import CardDeck


class JokerDeck(CardDeck):

    def _build_deck(self):
        super()._build_deck()
        joker1 = ('one', 'Joker')
        joker2 = ('two', 'Joker')
        self._cards.append(joker1)
        self._cards.append(joker2)
