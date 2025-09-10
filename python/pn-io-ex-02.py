#!/usr/bin/env python3

"""
moje rozwiązanie
"""

str1 = 'My'
str2 = 'Name'
str3 = 'Is'
str4 = 'James'
sep = "**"

def joining(a, b, c, d, separator):
    sentence = (a + sep + b + sep + c + sep + d)
    print(sentence)

joining (str1, str2, str3, str4, sep)

"""
sep jest już gotowym parametrem
funkcji print. wystarczy:
"""

# str1 = 'My'
# str2 = 'Name'
# str3 = 'Is'
# str4 = 'James'
# print(str1, str2, str3, str4, sep='**')
