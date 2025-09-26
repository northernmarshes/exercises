#!/usr/bin/env python3
# -----task-source:-ai-generated------
# Zadanie 6: Policz częstotliwość znaków
# Mając dany string, stwórz słownik gdzie kluczami są znaki, a wartościami ich częstotliwość w stringu.

string1 = 'Jessa'
letters = {}

for char in string1:
    if char in letters:
        letters[char] += 1
    else:
        letters[char] = 1
print(letters)

# ----------- Future Tips: -----------
# Inny sposób przed dostęp do słownika:
# letters[char] = letters.get(char, 0) + 1
