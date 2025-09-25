#!/usr/bin/env python3
# Exercise 10: Read Line Number 4 from File

with open("test.txt", 'r') as file:
    line = file.readlines()[3]
    print (line)
file.close

# ----------- Future Tips: -----------
