# Create a tuple of 3 items.
# Try to modify the second item and observe the error.
# Print each item in the tuple using a loop.

# 💡 TIP:
# Tuples are like lists, but immutable (they cannot be changed).

tup = (1, 2, 3)
try:
    tup[1] = 99
except TypeError as e:
    print("Error:", e)
for item in tup:
    print(item)
