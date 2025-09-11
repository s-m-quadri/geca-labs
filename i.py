# Write a program that prints each item of a list on a new line.
# Then, print the index and value using a loop.

# 💡 TIP:
# Use `for item in list` and `enumerate(list)` for both item and index.
my_list = ['apple', 'banana', 'cherry', 'date']
for item in my_list:
    print(item)     
print("Using enumerate:")
for index, value in enumerate(my_list):
    print(f"Index: {index}, Value: {value}")    
                