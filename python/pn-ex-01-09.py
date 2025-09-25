#!/usr/bin/env python3
# Exercise 9: Check Palindrome Number
# Write a Python code to check if the given number is a palindrome. A palindrome number reads the same forwards and backward. For example, 545 is a palindrome number.

def is_a_palind (num):
    num = str(num)
    rev_num = num[::-1]
    if num == rev_num:
        print ("The number is a palindrome.")
    else:
        print ("The number is not a palindrome.")

is_a_palind(202)
is_a_palind(102)

# ----------- Future Tips: -----------
