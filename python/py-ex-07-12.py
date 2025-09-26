#!/usr/bin/env python3
# -----task-source:-ai-generated------
# Zadanie 12: Usuń listę kluczy ze słownika
# Usuń określone klucze ze słownika.

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

keys_to_remove = {"name", "salary"}
new_dict = {k: v for k, v in sample_dict.items() if k not in keys_to_remove}

print(new_dict)

# ----------- Future Tips: -----------
# Nie można zniszczyć słownika w czasie
# iteracji. Dobrą praktyką jest stworzenie
# nowego z wyjątkiem kluczy oznaczonych do
# pominięcia.
# Schemat dictionary comprehension:
# new_dict = {k: v for k, v in my_dict.items() if k not in keys_to_remove}
