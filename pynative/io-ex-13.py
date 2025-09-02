#!/usr/bin/env python3
word = input("Enter a word: ")
number = input("Enter a number: ")
output = word + number
print (output.rjust(20))

# # na stronie, o dziwo, podejście
# # bardziej nowoczesne:
# word = input("Enter a word: ")
# number = input("Enter a number: ")
# print(f"{word:>20}{number}")
