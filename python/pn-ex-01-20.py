#!/usr/bin/env python3
# -----task-source:-pynative.com------
# Exercise 20: Print Reverse Number Pattern
# Expected Output:
# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4
# 5

rows = 5
b = 0

for i in range(rows,0,-1):
    b += 1
    for j in range (1,i+1):
        print(b, end = " ")
    print()

# ----------- Future Tips: -----------
