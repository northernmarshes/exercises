#!/usr/bin/env python3
for i in range(1,11):
    for j in range(1,11):
        mult = i * j
        if len(str(mult)) > 1:
            print (i * j, end=" ")
        else:
            print(i * j, end="  ")
    print() # nowa linia
