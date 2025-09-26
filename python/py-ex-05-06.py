#!/usr/bin/env python3
# -----task-source:-ai-generated------
# Zadanie 6: Przecięcie zbiorów i usuwanie
# Napisz kod znajdący przecięcie (wspólne elementy) dwóch zbiorów i usuń te elementy z pierwszego zbioru.

first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

def intersection_pop(first, second):
    """znajduje przecięcie i usuwa z pierwszego zbioru"""
    intersection = first & second
    first_after_removal = first - intersection
    print(f"Intersection is {intersection}")
    print(f"First set after removing common element is {first_after_removal}")
intersection_pop(first_set, second_set)


# ----------- Future Tips: -----------
# generalnie wszystko okej!
# jeśli w zespole są osoby nie znające pythona można
# postawić na większą czytelność jako, że “Readability counts”
# & jest bardziej pythoniczne ale dla czytelności
# można zamienić .intersection(second_set)
# można też usunąć elementy na stałe co jednak byłoby
# bardziej destrukcyjne:
# for item in intersection:
#    first_set.remove(item)
