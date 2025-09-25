#!/usr/bin/env python3
# Exercise 17: Generate Fibonacci series up to 15 terms
# Have you ever wondered about the Fibonacci Sequence? It’s a series of numbers in which the next number is found by adding up the two numbers before it. The first two numbers are 0 and 1.
# For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series is 13 + 21 = 34.

fibonacci = [0, 1]
for num in range(1, 14):
    fibonacci.append(fibonacci[-2] + fibonacci[-1])
print ("Fibonacci sequence:")
for val in fibonacci:
    print(val, end = ', ')

# ----------- Future Tips: -----------
