# Write a program that prints each item of a list on a new line.
# Then, print the index and value using a loop.

# 💡 TIP:
# Use `for item in list` and `enumerate(list)` for both item and index.

colors = ["blue","red","yellow","pink","green"]
for color in colors :
    print(color)

for index, value in enumerate(colors):
    print(f"Index {index}: {value}")