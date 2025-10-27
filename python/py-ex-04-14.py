#!/usr/bin/env python3
# -----task-source:-ai-generated------
# Zadanie 14: Usuń puste stringi z listy stringów

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]


def remove_empty_strings(strings):
    new_list = []
    for string in strings:
        if string:
            new_list.append(string)
    return new_list


print(remove_empty_strings(str_list))


#  ----------- Future Tips: -----------
#  wystarczy sprawdzić if na zmiennej
#  jeśli jest niepusta odda True
