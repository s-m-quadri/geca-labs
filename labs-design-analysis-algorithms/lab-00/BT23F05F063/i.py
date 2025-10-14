# Write a program that prints each item of a list on a new line.
# Then, print the index and value using a loop.

# 💡 TIP:
# Use `for item in list` and `enumerate(list)` for both item and index.

fruits = ["apple", "banana", "orange", "grape", "mango"]

print("Items:")
for fruit in fruits:
    print(fruit)

print("\nIndex and Items:")
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")
