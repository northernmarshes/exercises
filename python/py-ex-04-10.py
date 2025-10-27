#!/usr/bin/env python3
# -----task-source:-ai-generated------
# Zadanie 10: Policz wystąpienia wszystkich znaków w stringu
# Napisz program liczący wystąpienia wszystkich znaków w stringu.

str1 = "Apple"


def letter_count(word):
    letters = []
    counts = {}
    for char in word:
        letters.append(char)
    for char in letters:
        counts[char] = letters.count(char)
    print(counts)


letter_count(str1)
#  ----------- Future Tips: -----------
#  all fine
