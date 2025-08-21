# Write a program that prints each item of a list on a new line.
# Then, print the index and value using a loop.

# 💡 TIP:
# Use `for item in list` and `enumerate(list)` for both item and index.
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)



for index, value in enumerate(fruits):
    print(f"Index {index}: {value}")