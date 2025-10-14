# Create a function `greet` that takes a name and an optional message.
#  - If no message is provided, it should default to "Hello".
#  - Call the function in three different ways using default and named arguments.

# 💡 TIP:
#  Use `def greet(name, msg="Hello"):` to set a default value.

def greet(name, msg="Hello"):
    print(f"{msg}, {name}!")

greet("Alice")
greet("Bob", "Welcome")
greet(name="Charlie", msg="Hi")

def void_function():
    print("Running")

def add(a, b):
    return a + b

print(void_function())
print(add(2, 3))
