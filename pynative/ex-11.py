#!/usr/bin/env python3
number = 7536

def reverse (num):
    str_num = str(num)
    rev_num = str_num[::-1]
    result = ' '.join(rev_num)
    return result

print (reverse(number))
