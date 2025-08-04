# Write two functions:
#  - `void_function()` prints "Running" but returns nothing.
#  - `add(a, b)` returns the sum of a and b.
#  - Print the return values of both and observe the difference.

# 💡 TIP:
# All Python functions return something, even if it's just `None`.

def void_function():
    print("running")
def add(a,b):
    return a+b,
result1=void_function();
result2=add(10,5);
print('void function is:',result1);
print('Addition of 2 number is :',result2);
