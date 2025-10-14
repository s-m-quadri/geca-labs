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

# Test void function
print("Result of void_function():", void_function())

# Test add function
print("Result of add(3, 4):", add(3, 4))
