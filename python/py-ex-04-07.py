#!/usr/bin/env python3
# -----task-source:-ai-generated------
# Zadanie 7: Test balansu znaków stringów
# Napisz program sprawdzający czy dwa stringi są zbalansowane. Stringi s1 i s2 są zbalansowane jeśli wszystkie znaki z s1 są obecne w s2.

s1 = "Yn"
s2 = "PYnative"


def isbalanced(text01, text02):
    for char in text01:
        if char not in text02:
            return False
        else:
            return True


print(isbalanced(s1, s2))

#  ----------- Future Tips: -----------
# nazwa funkcji lepiej are_balanced
# szukamy "not in"
