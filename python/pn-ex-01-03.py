#!/usr/bin/env python3
# -----task-source:-pynative.com------
# Exercise 3: Print characters present at an even index number
# Write a Python code to accept a string from the user and display characters present at an even index number.

word = input ('Give me a word\n')

print (f'Orginal String is {word}\nPrinting only even index chars:')


for i, char in enumerate(word):
    if i % 2 == 0:
        print (char)

# ----------- Future Tips: -----------
# Moje rozwiązanie okazało się lepsze!
# Inne moje próby:
# even_letters = []
# for i in range(len(word)):
#     if i % 2 ==0:
#         even_letters.append(word[i])
# print (even_letters)
# print (word[::2])
#
# Rozwiązanie ze strony:
# word = input('Enter word ')
# print("Original String:", word)
# size = len(word)
# print("Printing only even index chars")
# for i in range(0, size - 1, 2):
#     print("index[", i, "]", word[i])
