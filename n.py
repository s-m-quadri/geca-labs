# Write a function that takes two numbers and returns their sum.
# Call it with example values and print the result.

# 💡 TIP:
# Use `def`, `return`, and call it like `f(2, 3)`.

def add(a, b):
    return a + b

result = add(5, 7)
print(result)

# Write a function that takes a name and a message and prints a greeting.
# Call it with example values and print the result.

def greet(name, msg="Hello"):
    print(f"{msg}, {name}!")

greet("Alice")
greet("Bob", "Welcome")
greet(name="Charlie", msg="Hi")

def void_function():
    print("Running")

print(void_function())
print(add(2, 3))
