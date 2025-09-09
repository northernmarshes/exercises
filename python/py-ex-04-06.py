#!/usr/bin/env python3

s1 = "Abc"
s2 = "Xyz"

def mixstrings(one, two):
    for char in one, two:
        print (one[1], two[-1])

print(mixstrings(s1,s2))
