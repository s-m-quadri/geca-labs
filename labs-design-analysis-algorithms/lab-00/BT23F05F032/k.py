# Create a tuple of 3 items.
# Try to modify the second item and observe the error.
# Print each item in the tuple using a loop.

# 💡 TIP:
# Tuples are like lists, but immutable (they cannot be changed).

my_tuple = ("red", "green", "blue")

try:
    my_tuple[1] = "yellow"
except TypeError as e:
    print("Error:", e)


for item in my_tuple:
    print(item)
