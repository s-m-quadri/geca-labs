# Create a tuple of 3 items.
# Try to modify the second item and observe the error.
# Print each item in the tuple using a loop.

# 💡 TIP:
# Tuples are like lists, but immutable (they cannot be changed).

colors = ("red", "green", "blue")

try:
    colors[1] = "yellow"  # This will raise an error
except TypeError as e:
    print(f"Error: {e}")

print("\nTuple items:")
for color in colors:
    print(color)
