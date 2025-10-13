# Write two functions:
#  - `void_function()` prints "Running" but returns nothing.
#  - `add(a, b)` returns the sum of a and b.
#  - Print the return values of both and observe the difference.

# 💡 TIP:
# All Python functions return something, even if it's just `None`.
# Function that prints but doesn't return anything
def void_function():
    print("Running")

def add(a, b):
    return a + b

result_void = void_function()  
result_add = add(5, 3)

print("Return value of void_function():", result_void)
print("Return value of add(5, 3):", result_add)
