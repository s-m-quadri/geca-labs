# Create a tuple of 3 items.
# Try to modify the second item and observe the error.
# Print each item in the tuple using a loop.

# 💡 TIP:
# Tuples are like lists, but immutable (they cannot be changed).
fruits = ("apple", "banana", "cherry")

# fruits[1] = "mango"  # This will cause a TypeError

for item in fruits:
    print(item)
