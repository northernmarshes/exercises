# #!/usr/bin/env python3
# Exercise 22: Capitalize the first letter of each word in a string

def capitalize(str1):
    print (str1.title())

sentence = "pynative.com is for python lovers"
capitalize(sentence)

# ----------- Future Tips: -----------
# Najlepsze rozwiązanie obsługujące apostrofy:
# def capitalize_words(text):
#    return " ".join(word.capitalize() for word in text.split())
