#!/usr/bin/env python3
# Exercise 2: Format Output String
# Write a program to display four string “My, “Name“, “Is“, “James” as “My**Name**Is**James“.
# Use the print() function to format the given words in the specified format. Display the ** separator between each string.

str1 = 'My'
str2 = 'Name'
str3 = 'Is'
str4 = 'James'
sep = "**"

def joining(a, b, c, d, separator):
    sentence = (a + sep + b + sep + c + sep + d)
    print(sentence)

joining (str1, str2, str3, str4, sep)


# ----------- Future Tips: -----------
# sep jest już gotowym parametrem
# funkcji print. wystarczy:
# str1 = 'My'
# str2 = 'Name'
# str3 = 'Is'
# str4 = 'James'
# print(str1, str2, str3, str4, sep='**')
