
# Write a program that prints each item of a list on a new line.
# Then, print the index and value using a loop.

# 💡 TIP:
# Use `for item in list` and `enumerate(list)` for both item and index.

# Create a sample list
my_list = ["apple", "banana", "cherry", "date", "elderberry"]

# Print each item on a new line
print("Items in the list:")
for item in my_list:
    print(item)

print()  

print("Index and value pairs:")
for index, value in enumerate(my_list):
    print(f"Index {index}: {value}")