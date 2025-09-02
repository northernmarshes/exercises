#!/usr/bin/env python3

numbers_list = [10, 20, 33, 46, 55]

def divisible_by_5 (x):
    for val in x:
        if val % 5 == 0:
            print (val)

print (f"Given list is {numbers_list}\nDivisible by 5")
divisible_by_5 (numbers_list)

# bardzo podobne
# num_list = [10, 20, 33, 46, 55]
# print("Given list:", num_list)
# print('Divisible by 5:')
# for num in num_list:
#     if num % 5 == 0:
#         print(num)
