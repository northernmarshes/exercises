#!/usr/bin/env python3
# Exercise 8: Print the following pattern
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
 
for x in (1,2,3,4,5):
    print (str(x)*x)

# ----------- Future Tips: -----------
# Rozwiązanie z podwójną pętlą
# for num in range(10):
#    for i in range(num):
#        print (num, end=" ") # print number
#    # new line after each row to display pattern correctly
#    print("\n")
# Poprawne:
# for num in range(1, 6):
#     for i in range(num):
#         print(num, end=" ")
#     print()  # nowa linia po każdym wierszu
