#!/usr/bin/env python3
# -----task-source:-ai-generated------
# Zadanie 7: Podzbiór lub nadzbiór innego zbioru
# Napisz kod sprawdzający czy jeden zbiór jest podzbiorem lub nadzbiorem innego zbioru. Jeśli tak, usuń wszystkie elementy z tego zbioru.

first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}


def issubset(set1, set2):
    if set1.issubset(set2):
        set1.clear()
        print("First set is a subset - contet cleared.")
        print(f"First set: {set1}")
    elif set1.issuperset(set2):
        set1.clear()
        print("First set is a superset - contet cleared.")
        print(f"First set: {set1}")
    else:
        print("Frist set is neither subset nor superset.")


issubset(first_set, second_set)

#  ----------- Future Tips: -----------
# próbowałam w ten sposób ale to nie działa
# niezależnie od sublet/superset:
# set_elements = len(set1)
# intersection_length = len(set1 & set2)
# if set_elements == intersection_length:
# set1.clear()
