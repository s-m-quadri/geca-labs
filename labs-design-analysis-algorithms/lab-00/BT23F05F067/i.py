# Write a program that prints each item of a list on a new line.
# Then, print the index and value using a loop.

# 💡 TIP:
# Use `for item in list` and `enumerate(list)` for both item and index.


items = ["apple", "banana", "cherry", "date"]

# Print each item on a new line
for item in items:
    print(item)

# Print index and value using enumerate
for index, value in enumerate(items):
    print("Index:", index, "Value:", value)
