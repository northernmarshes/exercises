#!/usr/bin/env python3
# -----task-source:-ai-generated------
# Zadanie 8: Znajdź wszystkie wystąpienia podstringa ignorując wielkość liter
# Napisz program znajdący wszystkie wystąpienia "USA" w danym stringu ignorując wielkość liter.

str1 = "Welcome to USA. usa awesome, isn't it?"
str2 = "USA"


def count_substring(text01, text02):
    text01_lower = text01.lower()
    text02_lower = text02.lower()
    sub_count = text01_lower.count(text02_lower)
    return sub_count


print(count_substring(str1, str2))

#  ----------- Future Tips: -----------
#  wykonując lower/upper zapisać do zmiennej
