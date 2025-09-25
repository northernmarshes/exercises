#!/usr/bin/env python3
# Zadanie 4: Policz wystąpienia każdego elementu z listy
# Napisz program iterujący przez daną listę, liczący wystąpienia każdego elementu i tworzący słownik pokazujący liczbę każdego elementu.

sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

def elements_dict(elements):
    e_dict = {}
    for element in elements:
        e_dict[element] = e_dict.get(element, 0) + 1
    return e_dict

print(elements_dict(sample_list))

# ----------- Future Tips: -----------
# dodawanie do słownika przez get()
