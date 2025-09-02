#!/usr/bin/env python3

numbers_x = [10, 20, 30, 40, 10]
# output True
numbers_y = [75, 65, 35, 75, 30]
# Output False

def even (x):
    if x[0] == x[4]:
        print ("True")
    else:
        print ("False")

even (numbers_x)
even (numbers_y)

# pisząc [-1] mamy dostęp do ostatniego punktu na liście
# def first_last_same(numberList):
#     print("Given list:", numberList)

#     first_num = numberList[0]
#     last_num = numberList[-1]

#     if first_num == last_num:
#         return True
#     else:
#         return False

# numbers_x = [10, 20, 30, 40, 10]
# print("result is", first_last_same(numbers_x))

# numbers_y = [75, 65, 35, 75, 30]
# print("result is", first_last_same(numbers_y))
