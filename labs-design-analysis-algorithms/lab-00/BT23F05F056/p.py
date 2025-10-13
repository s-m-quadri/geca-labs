# Write two functions:
#  - `void_function()` prints "Running" but returns nothing.
#  - `add(a, b)` returns the sum of a and b.
#  - Print the return values of both and observe the difference.

# 💡 TIP:
# All Python functions return something, even if it's just `None`.
# Function that prints but returns nothing
def void_function():
    print("Running")

# Function that returns the sum
def add(a, b):
    return a + b

# Calling functions and printing return values
print("Return value of void_function():", void_function())
print("Return value of add(5, 3):", add(5, 3))
