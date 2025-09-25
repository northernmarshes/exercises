#!/usr/bin/env python3
# Exercise 15: Get an int value of base raises to the power of exponent
# Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
# Note here exp is a non-negative integer, and the base is an integer.

def exponent(base, exp):
    print (f"base = {base}")
    print (f"exponent = {exp}")
    result = base ** exp
    print (f"{base} raises to the power of {exp}: {result}")

exponent (2,5)
exponent (5,4)

# ----------- Future Tips: -----------
