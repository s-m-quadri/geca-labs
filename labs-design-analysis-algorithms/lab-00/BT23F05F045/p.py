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

x = void_function()
y = add(3, 5)

print("Return value of void", x)
print("Return value of add(1, 9):", y)
