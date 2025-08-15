# Write a program that prints each item of a list on a new line.
# Then, print the index and value using a loop.

# 💡 TIP:
# Use `for item in list` and `enumerate(list)` for both item and index.
list=[12,23,"abcd",34,'a']

for items in list:
    print(items)

for index, value in enumerate(list):
    print(f"index:{index} , value:{value}")
    