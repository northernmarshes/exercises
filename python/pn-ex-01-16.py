#!/usr/bin/env python3
# Exercise 16: Check Palindrome Number
# A palindrome number is a number that remains the same when its digits are reversed. In simpler terms, it reads the same forwards and backward. For example 121, 5005.
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
