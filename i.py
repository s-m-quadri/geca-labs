# Write a program that prints each item of a list on a new line.
# Then, print the index and value using a loop.

# 💡 TIP:
# Use `for item in list` and `enumerate(list)` for both item and index.

list = [1,2,3,4,5]
for item in list:
    print(item)

for i,item in enumerate(list):
    print(i," ",item)