#!/usr/bin/env python3
# -----task-source:-pynative.com------
# Exercise 2: Print the Sum of a Current Number and a Previous number
# Write Python code to iterate through the first 10 numbers and, in each iteration, print the sum of the current and previous number.

previous = 0

for i in range(0, 10):
    print (f'Current Number {i} Previous Number {previous} Sum: {i + previous}')
    previous = i

# ----------- Future Tips: -----------
# To samo ale ze wskazówkami, trudnością było ogarnięcie zmiennej
# previous tak by wskazywała 0 w momencie kiedy numer to też 0
#
# previous_num = 0
# for i in range(1, 11):
#     x_sum = previous_num + i
#     print("Current Number", i, "Previous Number ", previous_num, " Sum: ", x_sum)
#     previous_num = i
