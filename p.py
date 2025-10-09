# Write two functions:
#  - `void_function()` prints "Running" but returns nothing.
#  - `add(a, b)` returns the sum of a and b.
#  - Print the return values of both and observe the difference.

# 💡 TIP:
# All Python functions return something, even if it's just `None`.

def void_function():
    print("Running")
    return None

def add(a, b):
    return a + b
# Testing the functions
result_void = void_function()
result_add = add(3, 5)
print("Return value of void_function():", result_void)
print("Return value of add(3, 5):", result_add)