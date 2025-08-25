# Write two functions:
#  - `void_function()` prints "Running" but returns nothing.
#  - `add(a, b)` returns the sum of a and b.
#  - Print the return values of both and observe the difference.

# 💡 TIP:
# All Python functions return something, even if it's just `None`.
# Define a void function (returns None)
def void_function():
    print("Running")

# Define a function that returns the sum of two numbers
def add(a, b):
    return a + b

# Call and print the return values
print("Return value of void_function():", void_function())  # Returns None
print("Return value of add(3, 4):", add(3, 4))              # Returns 7
