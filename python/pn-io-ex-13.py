#!/usr/bin/env python3
# Exercise 13: Display Right-Aligned Output
# Ask the user for a word and a number. Print the word right-aligned in a field of width 20, followed by the number.

word = input("Enter a word: ")
number = input("Enter a number: ")
output = word + number
print (output.rjust(20))

# ----------- Future Tips: -----------
# Na stronie podejście bardziej nowoczesne:
# word = input("Enter a word: ")
# number = input("Enter a number: ")
# print(f"{word:>20}{number}")
