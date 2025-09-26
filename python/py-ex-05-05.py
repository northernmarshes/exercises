#!/usr/bin/env python3
# -----task-source:-ai-generated------
# Zadanie 5: Sparowane elementy z dwóch list jako zbiór
# Napisz kod tworzący zbiór Pythona pokazujący elementy z obu list w parach.
# Oczekiwany wynik: {(6, 36), (8, 64), (4, 16), (5, 25), (3, 9), (7, 49), (2, 4)}

first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]

def merge_lists(first, second):
    """merges two lists into a dictionary"""
    merge = {}
    for f, s in zip(first,second):
        merge[f] = merge.get(f, s)
    return merge
print(merge_lists(first_list, second_list))

# ----------- Future Tips: -----------
# program returs a dictionary not a set!
# read carefully!
# powinno być: set(zip(first,second))
