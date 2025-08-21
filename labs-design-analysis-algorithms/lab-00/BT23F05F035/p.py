# Write two functions:
#  - `void_function()` prints "Running" but returns nothing.
#  - `add(a, b)` returns the sum of a and b.
#  - Print the return values of both and observe the difference.

# 💡 TIP:
# All Python functions return something, even if it's just `None`.

def void_function():
    print("Running")

def add(a, b):
    return a + b

# Calling functions and printing their return values
print("Return value of void_function():", void_function())
print("Return value of add(5, 3):", add(5, 3))
