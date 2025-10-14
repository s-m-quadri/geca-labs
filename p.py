# Function that prints but returns nothing
def void_function():
    print("Running")

# Function that returns a value
def add(a, b):
    return a + b

# Call both functions
result1 = void_function()
result2 = add(5, 3)

# Print return values
print("Return value of void_function():", result1)
print("Return value of add(5, 3):", result2)
