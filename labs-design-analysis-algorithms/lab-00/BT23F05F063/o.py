# Create a function `greet` that takes a name and an optional message.
#  - If no message is provided, it should default to "Hello".
#  - Call the function in three different ways using default and named arguments.

# 💡 TIP:
#  Use `def greet(name, msg="Hello"):` to set a default value.

def greet(name, msg="Hello"):
    return f"{msg}, {name}!"

# Using default message
print(greet("Alice"))

# Providing a custom message
print(greet("Bob", "Hi"))

# Using named arguments
print(greet(msg="Good morning", name="Charlie"))
