#!/usr/bin/env python3
# -----task-source:-ai-generated------
# Zadanie 13: Sprawdź czy wartość istnieje w słowniku
# Napisz program Python który sprawdza czy wartość 200 jest obecna w podanym słowniku.

sample_dict = {'a': 100, 'b': 200, 'c': 300}
values = sample_dict.values()

if 200 in values:
    print("200 present in a dict")
else:
    print("200 not present in a dict")

# ----------- Future Tips: -----------
# Łatwiej najpierw wyciągnąć wartości
# niż od razu iterować.
