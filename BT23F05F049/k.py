# Create a tuple of 3 items.
# Try to modify the second item and observe the error.
# Print each item in the tuple using a loop.

# 💡 TIP:
# Tuples are like lists, but immutable (they cannot be changed).
tuple=(5,15,25)
# tuple[1]=10 --> TypeError: 'tuple' object does not support item assignment
for i in tuple:
    print(i)