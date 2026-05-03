# Create a list of 5 integers.
# Print the first, middle, and last elements.
# Modify the third element to be 100, then print the entire list.

# 💡 TIP:
# Use indexing like list[0], list[-1], and list[2] to access or change values.
my_list = [10, 20, 30, 40, 50]
print("First:", my_list[0])
print("Middle:", my_list[len(my_list) // 2])
print("Last:", my_list[-1])

my_list[2] = 100
print("Modified List:", my_list)