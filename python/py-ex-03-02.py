#!/usr/bin/env python3

def func1(*args):
    for value in args:
        print(value)

func1("Kot", "Pies", 34, 3.25, True)
