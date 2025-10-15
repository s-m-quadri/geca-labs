# Create a tuple of 3 items.
# Try to modify the second item and observe the error.
# Print each item in the tuple using a loop.

# 💡 TIP:
# Tuples are like lists, but immutable (they cannot be changed).
# Create a tuple of 3 items.
# Try to modify the second item and observe the error.
# Print each item in the tuple using a loop.

# 💡 TIP:
# Tuples are like lists, but immutable (they cannot be changed).

my_tuple = (1, 2, 3)

# Uncomment the next line to see the error:
# my_tuple[1] = 99  # This will raise a TypeError

for item in my_tuple:
    print(item)