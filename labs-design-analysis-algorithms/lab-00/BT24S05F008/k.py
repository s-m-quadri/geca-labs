# Create a tuple of 3 items.
# Try to modify the second item and observe the error.
# Print each item in the tuple using a loop.

# 💡 TIP:
# Tuples are like lists, but immutable (they cannot be changed).

tup = (1,2,3)

# It gives this error : 'tuple' object does not support item assignment. 
# tup[1] = 100

for i in tup: 
    print(i)