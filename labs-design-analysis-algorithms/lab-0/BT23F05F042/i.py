# Write a program that prints each x of a list on a new line.
# Then, print the index and value using a loop.

# 💡 TIP:
# Use `for x in list` and `enumerate(list)` for both x and index.

list = [10, 20, 30, 40, 50]

for x in list:
    print(x)

for index, value in enumerate(list):
    print(f"Index: {index}, Value: {value}")
