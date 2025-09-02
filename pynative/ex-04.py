 #!/usr/bin/env python3
def remove_chars(word,n):
    length = len(word)
    new_word = word[n:length]
    return new_word


print("Removing characters from a string")
print(remove_chars("pynative", 4))
print(remove_chars("pynative", 2))

# Nie trzeba było zaznaczać długości słowa
# w ogóle:

# def remove_chars(word, n):
#     print('Original string:', word)
#     x = word[n:]
#     return x
