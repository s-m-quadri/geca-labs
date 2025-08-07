# Write a program that prints each item of a list on a new line.
# Then, print the index and value using a loop.

# 💡 TIP:
# Use `for item in list` and `enumerate(list)` for both item and index.

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Print each item on a new line
for fruit in fruits:
    print(fruit)

# Print index and value
for index, fruit in enumerate(fruits):
    print(index, fruit)
