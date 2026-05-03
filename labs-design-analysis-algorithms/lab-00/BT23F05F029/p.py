# Write two functions:
#  - `void_function()` prints "Running" but returns nothing.
#  - `add(a, b)` returns the sum of a and b.
#  - Print the return values of both and observe the difference.

# 💡 TIP:
# All Python functions return something, even if it's just `None`.

# Define a function that prints but doesn't return anything
def void_function():
    print("Running")   # prints something
    # no return statement → implicitly returns None

# Define a function that returns the sum of a and b
def add(a, b):
    return a + b

# Call both functions and print their return values
print("Return value of void_function():", void_function())
print("Return value of add(5, 7):", add(5, 7))
