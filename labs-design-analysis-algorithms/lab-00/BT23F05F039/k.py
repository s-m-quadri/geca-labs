# Create a tuple of 3 items.
# Try to modify the second item and observe the error.
# Print each item in the tuple using a loop.

# 💡 TIP:
# Tuples are like lists, but immutable (they cannot be changed).

my_tuple = ("apple", "banana", "cherry")

print("Original tuple:", my_tuple)

try:
    my_tuple[1] = "orange"
except TypeError as e:
    print(f"Error when trying to modify tuple: {e}")

print("\nItems in the tuple:")
for item in my_tuple:
    print(item)