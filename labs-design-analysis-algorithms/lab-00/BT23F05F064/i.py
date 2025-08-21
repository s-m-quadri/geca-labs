# Write a program that prints each item of a list on a new line.
# Then, print the index and value using a loop.

# 💡 TIP:
# Use `for item in list` and `enumerate(list)` for both item and index.

a = [1,2,3,4,5]
for item in a:
    print(item)

for index, value in enumerate(a):
    print(index,value)