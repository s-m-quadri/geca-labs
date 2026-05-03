# Write a program that prints each item of a list on a new line.
# Then, print the index and value using a loop.

# 💡 TIP:
# Use `for item in list` and `enumerate(list)` for both item and index.
list=["tomato","potato","bong bong"]
for i in list:
    print(i)

for i,j in enumerate(list):
    print(i,j)