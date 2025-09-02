#!/usr/bin/env python3
def menu():
    while True:
        command = input ("Select a number and press [Enter]:\n 1. Say Hello\n 2. Calculate Square\n 3. Exit\n")
        if command == "1":
            print ("Hello!")
        elif command == "2":
            base = int(input("Give me a base to square "))
            squared = base ** 2
            print(squared)
        elif command == "3":
            break
        else:
            print("Your answer is not 1, 2, or 3!")

menu()

# # program jest okej, możliwe sugestie to,
# # obsługa błędów:
# elif command == "2":
#     try:
#         base = int(input("Give me a base to square: "))
#         squared = base ** 2
#         print(f"The square of {base} is {squared}")
#     except ValueError:
#         print("Please enter a valid number!")
# # i formatowanie:
# print("\nMenu:")
# print("1. Say Hello")
# print("2. Calculate Square")
# print("3. Exit")
# command = input("Enter your choice (1-3): ")
