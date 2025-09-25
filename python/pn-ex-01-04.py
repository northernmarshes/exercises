#!/usr/bin/env python3
# Exercise 4: Remove first n characters from a string
# Write a Python code to remove characters from a string from 0 to n and return a new string.

def remove_chars(word,n):
    length = len(word)
    new_word = word[n:length]
    return new_word


print("Removing characters from a string")
print(remove_chars("pynative", 4))
print(remove_chars("pynative", 2))

# ----------- Future Tips: -----------
# Nie trzeba było w ogóle zaznaczać długości słowa:
#
# def remove_chars(word, n):
#     print('Original string:', word)
#     x = word[n:]
#     return x
