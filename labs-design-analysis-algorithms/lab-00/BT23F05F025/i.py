# Write a program that prints each item of a list on a new line.
# Then, print the index and value using a loop.

# 💡 TIP:
# Use `for item in list` and `enumerate(list)` for both item and index.

list = [10, 20, 30, 40, 50]
for item in list:
    print(item)

for index, value in enumerate(list):
        print(index, value)
