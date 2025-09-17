#!/usr/bin/env python3
# POZIOM 5: Python Data Structure Exercise (Zadania 1-10)
# Zadanie 2: Usuń i dodaj element w liście

list1 = [54, 44, 27, 79, 91, 41]
item = list1.pop(4)
list1.insert(1,item)
list1.append(item)
print(list1)
