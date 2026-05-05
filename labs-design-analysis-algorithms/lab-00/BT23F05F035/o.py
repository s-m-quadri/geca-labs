# Create a function `greet` that takes a name and an optional message.
#  - If no message is provided, it should default to "Hello".
#  - Call the function in three different ways using default and named arguments.

# 💡 TIP:
#  Use `def greet(name, msg="Hello"):` to set a default value.

def greet(name, message="Hello"):
    print(f"{message}, {name}!")

# Calling the function in three different ways
greet("Alice")  # Using default message
greet("Bob", "Good morning")  # Providing a custom message
greet(name="Charlie", message="Welcome")  # Using named arguments
