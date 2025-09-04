#!/usr/bin/env python3
def string_split(word):
    first = (word[0])
    middle = (word[round(len(word)/2)])
    last = (word[-1])
    print (first+middle+last)

str1 = "James"
str2 = "Konstantynopolitańczykowianeczka"
str3 = "James"
string_split(str1)
string_split(str2)
