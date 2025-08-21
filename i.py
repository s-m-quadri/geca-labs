# Write a program that prints each item of a list on a new line.
# Then, print the index and value using a loop.

# 💡 TIP:
# Use `for item in list` and `enumerate(list)` for both item and index.
lists= [2,4,0, 6,5]
for list in lists:
    print(list)


for index, value in enumerate(lists):
    print(f"Index {index}: {value}")