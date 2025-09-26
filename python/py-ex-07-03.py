#!/usr/bin/env python3
# -----task-source:-ai-generated------
# Zadanie 3: Słownik z list
# Napisz program Python który konwertuje dwie listy Python na słownik, gdzie elementy z pierwszej listy stają się kluczami, a elementy z drugiej listy stają się wartościami.

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
numbers = {}

for k, v in zip(keys, values):
    numbers[k] = v

print(numbers)

# ----------- Future Tips: -----------
# napisane z ręki i działa za pierwszym
# razem, brawa dla mnie ;d
# jednakże... można było prościej:
# result_dict = dict(zip(keys, values))
