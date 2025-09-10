#!/usr/bin/env python3
for x in (1,2,3,4,5):
    print (str(x)*x)

# # Rozwiązanie z podwójną pętlą
#  for num in range(10):
#     for i in range(num):
#         print (num, end=" ") # print number
#     # new line after each row to display pattern correctly
#     print("\n")

# Poprawne:
# for num in range(1, 6):
#     for i in range(num):
#         print(num, end=" ")
#     print()  # nowa linia po każdym wierszu
