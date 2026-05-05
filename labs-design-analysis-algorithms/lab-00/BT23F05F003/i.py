# Write a program that prints each item of a list on a new line.
# Then, print the index and value using a loop.

# 💡 TIP:
# Use `for item in list` and `enumerate(list)` for both item and index.

list = [2,4,6,8,10]

for item in list:
    print(item)

for index,value in enumerate(list):
    print(f"{index} : {value}")
