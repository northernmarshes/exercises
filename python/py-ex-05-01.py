#!/usr/bin/env python3
# POZIOM 5: Python Data Structure Exercise (Zadania 1-10)
# Zadanie 1: Tworzenie listy używając dwóch list

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

del l1[::2]
result = l1+l2[::2]

print(result)

# future tips:
# best create odd numbers
# with l1[1::2]
