# Create a tuple of 3 items.
# Try to modify the second item and observe the error.
# Print each item in the tuple using a loop.

# 💡 TIP:
# Tuples are like lists, but immutable (they cannot be changed).

# Creating a tuple with 3 items
colors = ("red", "green", "blue")

# Try to modify the second item (this will cause an error)
try:
    colors[1] = "yellow"
except TypeError as e:
    print("Error:", e)

# Print each item using a loop
print("\nItems in the tuple:")
for color in colors:
    print(color)
