#!/usr/bin/env python3
# -----task-source:-pynative.com------
# Exercise 13: Print multiplication table from 1 to 10
# The multiplication table from 1 to 10 is a table that shows the products of numbers from 1 to 10.
# Write a code to generates a complete multiplication table for numbers 1 through 10.

for i in range(1,11):
    for j in range(1,11):
        mult = i * j
        if len(str(mult)) > 1:
            print (i * j, end=" ")
        else:
            print(i * j, end="  ")
    print() # nowa linia

# ----------- Future Tips: -----------
