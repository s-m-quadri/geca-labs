# Ask the user for their name and age using `input()`.
# Then print: "Hello <name>, you are <age> years old."

# 💡 TIP:
# `input()` always returns a string, so use `int()` to convert age.
# Asking user for input
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Printing the message
print("Hello", name + ", you are", age, "years old.")
