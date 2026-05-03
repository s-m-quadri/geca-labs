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

result1 = void_function()
result2 = add(3, 4)

print("Return value of void_function():", result1)
print("Return value of add(3, 4):", result2)
