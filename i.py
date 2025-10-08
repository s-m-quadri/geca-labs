# Write a program that prints each item of a list on a new line.
# Then, print the index and value using a loop.

# 💡 TIP:
# Use `for item in list` and `enumerate(list)` for both item and index.

#solution
items = ["apple", "banana", "cherry", "date"]
for item in items:
    print(item)

for idx, val in enumerate(items):
    print(f"Index {idx}: {val}")