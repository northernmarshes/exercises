#!/usr/bin/env python3
# -----task-source:-ai-generated------
# Zadanie 11: Stwórz słownik poprzez wyodrębnienie kluczy z danego słownika
# Napisz program Python który tworzy nowy słownik poprzez wyodrębnienie wspomnianych kluczy z poniższego słownika.

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
new_dict = {}

for key in sample_dict:
    if key == "name" or key == "salary" :
        new_dict[key] = sample_dict.get(key)
print (new_dict)

# ----------- Future Tips: -----------
# pay attention to the variable names
