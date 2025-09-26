#!/usr/bin/env python3
# -----task-source:-pynative.com------
# Exercise 17: Generate Fibonacci series up to 15 terms

fibonacci = [0, 1]
for num in range(1, 14):
    fibonacci.append(fibonacci[-2] + fibonacci[-1])
print ("Fibonacci sequence:")
for val in fibonacci:
    print(val, end = ', ')

# ----------- Future Tips: -----------
