# Write two functions:
#  - `void_function()` prints "Running" but returns nothing.
#  - `add(a, b)` returns the sum of a and b.
#  - Print the return values of both and observe the difference.

# 💡 TIP:
# All Python functions return something, even if it's just `None`.

def void_function():
    print("Running")

def add(a,b):
    return a+b

ret1 = void_function()
ret2 = add(2,3)

print(ret1)
print(ret2)
