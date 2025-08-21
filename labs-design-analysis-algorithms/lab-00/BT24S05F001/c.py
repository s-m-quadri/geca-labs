# Ask the user for their name and age using `input()`.
# Then print: "Hello <name>, you are <age> years old."

# 💡 TIP:
# `input()` always returns a string, so use `int()` to convert age.


name = input("What is your name? ")
age = int(input("What is your age? "))

print("Hello", name + ", you are", age, "years old.")
