# Create a tuple of 3 items.
# Try to modify the second item and observe the error.
# Print each item in the tuple using a loop.

# 💡 TIP:
# Tuples are like lists, but immutable (they cannot be changed).
my_tuple = (10, 20, 30)

# Trying to modify the second item will raise an error
try:
    my_tuple[1] = 50
except TypeError as e:
    print("Error:", e)

# Print each item in the tuple
for item in my_tuple:
    print(item)
