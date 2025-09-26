#!/usr/bin/env python3
# -----task-source:-pynative.com------
# Exercise 21: Check if a user-entered string contains any digits using a for loop

sentence = input("Please enter a sentence.\n")
numbers = []
for char in sentence:
    if char.isdigit():
        numbers.append(char)
if numbers:
    print ("The string contains at least one digit.")
else:
    print ("The string does not contain any digits.")

# ----------- Future Tips: -----------
# Lepsza opcja - zachowuje zasadę
# early return i nie sprawdza wszystkich znaków:
#
# def contains_digits(text):
# for char in text:
#     if char.isdigit():
#         return True
# return False
#
# Inna możliwość znalezienia cyfry porównywanie
# wartości ascii:
# if '0' <= char <= '9':
