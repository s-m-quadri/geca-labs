# Create a tuple of 3 items.
# Try to modify the second item and observe the error.
# Print each item in the tuple using a loop.

# 💡 TIP:
# Tuples are like lists, but immutable (they cannot be changed).
#code
my_tuple = (10, 20, 30)
try:
    my_tuple[1] = 25
except TypeError as e:
    print(f"Error: {e}")
for item in my_tuple:
    print(item)