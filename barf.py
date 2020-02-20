#!/usr/bin/env python

class DessertTopping:

    def whoosh(self):
        print("Whoosh!")

class FloorWax:

    def shine(self):
        print("SHINY!")


class Barf(DessertTopping, FloorWax):
    pass


b = Barf()
b.whoosh()
b.shine()
