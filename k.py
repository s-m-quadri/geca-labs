# Create a tuple of 3 items.
# Try to modify the second item and observe the error.
# Print each item in the tuple using a loop.

# 💡 TIP:
# Tuples are like lists, but immutable (they cannot be changed).


# Create a tuple of 3 items
my_tuple = (10, 20, 30)

# Try to modify the second item (will cause an error)
# my_tuple[1] = 200  # Uncommenting this line will raise TypeError

# Print each item using a loop
print("Items in the tuple:")
for item in my_tuple:
    print(item)
