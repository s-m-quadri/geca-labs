# Write a program that prints each item of a list on a new line.
# Then, print the index and value using a loop.

# 💡 TIP:
# Use `for item in list` and `enumerate(list)` for both item and index.

fruits = ["apple", "banana", "cherry", "date", "elderberry"]


print("List items:")
for item in fruits:
    print(item)


print("\nIndex and items:")
for index, value in enumerate(fruits):
    print(f"Index {index}: {value}")
