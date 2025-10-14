# Write a program that prints each item of a list on a new line.
# Then, print the index and value using a loop.

# 💡 TIP:
# Use `for item in list` and `enumerate(list)` for both item and index.
fruits = ["apple", "banana", "cherry"]
for i in fruits:
    print(i)

print("------")

for j, fruitName in enumerate(fruits):
    print(f"Index {j}: {fruitName}")