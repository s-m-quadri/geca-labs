# Create a tuple of 3 items.
# Try to modify the second item and observe the error.
# Print each item in the tuple using a loop.

# 💡 TIP:
# Tuples are like lists, but immutable (they cannot be changed).
my_tuple = ("apple", "banana", "cherry")

# This line will cause an error because tuples are immutable
# my_tuple[1] = "mango"

for item in my_tuple:
    print(item)
