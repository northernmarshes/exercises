#!/usr/bin/env python3
# Zadanie 5: Scal dwa słowniki Python w jeden
# Napisz kod który scala dwa słowniki w nowy słownik i go wyświetla.
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict3 = dict1
dict3.update(dict2)
print(dict3)

# ----------- Future Tips: -----------
# inne metody:
# dict3 = dict1 | dict2
# dict3 = {**dict1, **dict2}
