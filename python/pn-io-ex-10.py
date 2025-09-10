#!/usr/bin/env python3
with open("test.txt", 'r') as file:
    line = file.readlines()[3]
    print (line)
file.close
