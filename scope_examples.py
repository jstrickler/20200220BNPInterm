#!/usr/bin/env python


x = 100  # global variable

def spam():
    y = 42  # local variable
    print(y)

    def ham():
        print("in ham(): y is", y)

    return ham

wombat = spam()

wombat()

