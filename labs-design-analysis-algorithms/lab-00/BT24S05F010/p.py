# Write two functions:
#  - `void_function()` prints "Running" but returns nothing.
#  - `add(a, b)` returns the sum of a and b.
#  - Print the return values of both and observe the difference.

# 💡 TIP:
# All Python functions return something, even if it's just `None`.

def add(a,b):
    return a+b

def void_function():
    print("running")

print(add(9,4))
print(void_function())