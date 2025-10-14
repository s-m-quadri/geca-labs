# Creating a tuple of 3 items
my_tuple = ("apple", "banana", "cherry")

# Trying to modify the second item (this will cause an error)
try:
    my_tuple[1] = "orange"
except TypeError as e:
    print("Error:", e)

# Printing each item using a loop
print("\nItems in the tuple:")
for item in my_tuple:
    print(item)
