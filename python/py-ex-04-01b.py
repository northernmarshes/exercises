#!/usr/bin/env python3
# Zadanie 1B: Stwórz string z trzech środkowych znaków
# Napisz program do stworzenia nowego stringa składającego się z trzech środkowych znaków danego stringa.


def middlechars(word):
    left = (word[(round(len(word)//2))-1])
    middle = (word[round(len(word)//2)])
    right = (word[(round(len(word)//2))+1])
    print(left + middle + right)

str1 = "JhonDipPeta"
str2 = "KonstantyKijKonstanty"
middlechars(str1)
middlechars(str2)

# ----------- Future Tips: -----------
# Lepiej byłoby zastosować wycinek:
# middle_index = len(text) // 2
# return text[middle_index-1:middle_index+2]
