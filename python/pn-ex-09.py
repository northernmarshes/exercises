#!/usr/bin/env python3
def is_a_palind (num):
    num = str(num)
    rev_num = num[::-1]
    if num == rev_num:
        print ("The number is a palindrome.")
    else:
        print ("The number is not a palindrome.")

is_a_palind(202)
is_a_palind(102)
