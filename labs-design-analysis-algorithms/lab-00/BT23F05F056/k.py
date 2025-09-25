# Create a tuple of 3 items.
# Try to modify the second item and observe the error.
# Print each item in the tuple using a loop.

# 💡 TIP:
# Tuples are like lists, but immutable (they cannot be changed).
# Creating a tuple of 3 items
my_tuple = ("red", "green", "blue")

# Trying to modify the second item (this will cause an error)
# Uncommenting the line below will raise: TypeError
# my_tuple[1] = "yellow"

# Printing each item using a loop
print("Tuple items:")
for item in my_tuple:
    print(item)
