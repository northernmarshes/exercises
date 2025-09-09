#!/usr/bin/env python3

str1 = "PyNaTive"

def lowerfirst(word):
    lower = ""
    upper = ""
    for char in word:
        if char.islower() == True:
            lower = lower + char
        elif char.isupper() == True:
            upper = upper + char
    newword = lower + upper
    print (newword)


lowerfirst(str1)

# możnaby zrezygnować z == True
# oraz zwracać wynik zamiast go
# drukować
