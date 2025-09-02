#!/usr/bin/env python3

"""moje rozwiązanie:"""

sentence = input("Please enter a sentence.\n")
numbers = []
for char in sentence:
    if char.isdigit():
        numbers.append(char)
if numbers:
    print ("The string contains at least one digit.")
else:
    print ("The string does not contain any digits.")

"""lepsza opcja - zachowuje zasadę
early return i nie sprawdza wszystkich znaków:"""

# def contains_digits(text):
# for char in text:
#     if char.isdigit():
#         return True
# return False

"""inna możliwość znalezienia cyfry porównywanie
wartości ascii"""

# if '0' <= char <= '9':
