# Write a program that prints each item of a list on a new line.
# Then, print the index and value using a loop.

# 💡 TIP:
# Use `for item in list` and `enumerate(list)` for both item and index.
items = ["pen", "pencil", "scale", "eraser"]
for item in items:
    print(item)
for index, value in enumerate(items):
    print(index, value)
