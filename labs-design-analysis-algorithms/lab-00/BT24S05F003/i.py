# Write a program that prints each item of a list on a new line.
# Then, print the index and value using a loop.

# 💡 TIP:
# Use `for item in list` and `enumerate(list)` for both item and index.

list=["apple","banana","orange"]

for i in list:
    print(i)



for index,value in enumerate(list):
    print(index,value)  
