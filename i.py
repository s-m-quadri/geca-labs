# Write a program that prints each item of a list on a new line.
# Then, print the index and value using a loop.

# 💡 TIP:
# Use `for item in list` and `enumerate(list)` for both item and index.

fruits = ["apple", "banana", "cherry", "date"]

print("Items:")
for item in fruits:
    print(item)

print("Index and value:")
for index, value in enumerate(fruits):
    print(f"{index}: {value}")
