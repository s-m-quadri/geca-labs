# Function that prints but returns nothing
def void_function():
    print("Running")

# Function that returns the sum of two numbers
def add(a, b):
    return a + b

result1 = void_function()
result2 = add(5, 7)

# Printing the return values
print("Return value of void_function():", result1)
print("Return value of add(5, 7):", result2)
