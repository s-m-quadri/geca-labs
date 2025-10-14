# Ask the user for their name and age using `input()`.
# Then print: "Hello <name>, you are <age> years old."

# 💡 TIP:
# `input()` always returns a string, so use `int()` to convert age.
# Ask the user for their name and age
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Print the message
print(f"Hello {name}, you are {age} years old.")
