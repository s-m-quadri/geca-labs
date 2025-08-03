# Create a list of 5 integers.
# Print the first, middle, and last elements.
# Modify the third element to be 100, then print the entire list.

# 💡 TIP:
# Use indexing like list[0], list[-1], and list[2] to access or change values.

list = [10, 20, 30, 40, 50]

print("First:", list[0])
print("Middle:", list[len(list) // 2])
print("Last:", list[-1])

list[2] = 100

print("New list:", list)
