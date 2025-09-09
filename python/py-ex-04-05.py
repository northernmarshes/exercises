#!/usr/bin/env python3

str1 = "P@#yn26at^&i5ve"

def countchars(word):
    chars = 0
    digits = 0
    symbols = 0
    for char in word:
        if char.isalpha():
            chars = chars + 1 # skróć do chars += 1
        elif char.isdigit():
            digits = digits + 1
        else:
            symbols= symbols + 1
    count = (f"Chars = {chars} Digits = {digits} Symbol = {symbols}")
    return count

print(countchars(str1))

# def count_chars(text):
#     chars = digits = symbols = 0

#     for char in text:
#         if char.isalpha():
#             chars += 1
#         elif char.isdigit():
#             digits += 1
#         else:
#             symbols += 1

#     return chars, digits, symbols

# str1 = "P@#yn26at^&i5ve"
# chars, digits, symbols = count_chars(str1)
# print(f"Chars = {chars} Digits = {digits} Symbol = {symbols}")
