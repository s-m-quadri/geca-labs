# Ask the user for their name and age using `input()`.
# Then print: "Hello <name>, you are <age> years old."

# 💡 TIP:
# `input()` always returns a string, so use `int()` to convert age.

name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello", name + ", you are", int(age), "years old.")
