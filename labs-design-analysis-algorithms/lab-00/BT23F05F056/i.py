# Write a program that prints each item of a list on a new line.
# Then, print the index and value using a loop.

# 💡 TIP:
# Use `for item in list` and `enumerate(list)` for both item and index.
# Creating a list
fruits = ["Apple", "Banana", "Cherry", "Mango"]

# Printing each item on a new line
print("Items in the list:")
for item in fruits:
    print(item)

# Printing index and value
print("\nIndex and values:")
for index, value in enumerate(fruits):
    print(index, value)
