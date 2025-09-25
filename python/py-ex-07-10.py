#!/usr/bin/env python3
# Zadanie 10: Zainicjalizuj słownik z domyślnymi wartościami
# W Pythonie możemy zainicjalizować klucze z tymi samymi wartościami.

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
data = {}

for employee in employees:
    data[employee] = defaults
print(data)

# ----------- Future Tips: -----------
# inny sposób:
# result = {emp: defaults.copy() for emp in employees}
