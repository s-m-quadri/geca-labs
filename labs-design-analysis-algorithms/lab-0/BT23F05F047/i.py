# Write a program that prints each item of a list on a new line.
# Then, print the index and value using a loop.

# 💡 TIP:
# Use `for item in list` and `enumerate(list)` for both item and index.


items = ["apple", "banana", "cherry", "date"]


print("Items in the list:")
for item in items:
    print(item)


print("\nIndex and value:")
for index, value in enumerate(items):
    print(f"Index {index}: {value}")
