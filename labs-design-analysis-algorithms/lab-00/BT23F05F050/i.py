# Write a program that prints each item of a list on a new line.
# Then, print the index and value using a loop.

# 💡 TIP:
# Use `for item in list` and `enumerate(list)` for both item and index.
 

grocery = ["teapowder", "sugar", "salt", "milk"]

print("Items in the list:")
for item in grocery:
    print(item)

print("\nIndex and value:")
for index, value in enumerate(grocery):
    print(f"Index {index}: {value}")
