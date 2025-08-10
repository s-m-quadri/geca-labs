# Write a program that prints each item of a list on a new line.
# Then, print the index and value using a loop.

# 💡 TIP:
# Use `for item in list` and `enumerate(list)` for both item and index.
list=['Math','English','Science','History']
print("Items in the list: ")
for item in list:
    print(item)
print("\nIndex and value in the list:")
for index,value in enumerate(list):
    print(f"Index {index}={value}")