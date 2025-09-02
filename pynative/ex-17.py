#!/usr/bin/env python3
fibonacci = [0, 1]
for num in range(1, 14):
    fibonacci.append(fibonacci[-2] + fibonacci[-1])
print ("Fibonacci sequence:")
for val in fibonacci:
    print(val, end = ', ')
