# Write a program that prints each item of a list on a new line.
# Then, print the index and value using a loop.

# 💡 TIP:
# Use `for item in list` and `enumerate(list)` for both item and index.

fruits = ["apple", "banana", "cherry", "mango"]

for item in fruits:
    print(item)

print("With index:")
for index, value in enumerate(fruits):
    print(index, value)
