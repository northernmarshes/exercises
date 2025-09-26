#!/usr/bin/env python3
# -----task-source:-pynative.com------
# Exercise 16: Check Palindrome Number
# Write a code to check if given number is palindrome.

num = input("Hit me with a number!\n")
def ispalindrome(num):
    reverse = str(num)[::-1]
    if num == reverse:
        print (f"{num} is a palindrome!")
    else:
        print (f"{num} is not a palindrome!")
ispalindrome(num)

# ----------- Future Tips: -----------
