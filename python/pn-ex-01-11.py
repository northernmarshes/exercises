#!/usr/bin/env python3
# Exercise 11: Get each digit from a number in the reverse order.
# For example, If the given integer number is 7536, the output shall be “6 3 5 7“, with a space separating the digits.

number = 7536

def reverse (num):
    str_num = str(num)
    rev_num = str_num[::-1]
    result = ' '.join(rev_num)
    return result

print (reverse(number))

# ----------- Future Tips: -----------
