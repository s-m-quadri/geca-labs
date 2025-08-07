# Create a function `greet` that takes a name and an optional message.
#  - If no message is provided, it should default to "Hello".
#  - Call the function in three different ways using default and named arguments.

# 💡 TIP:
#  Use `def greet(name, msg="Hello"):` to set a default value.

def greet(name, msg="Hello"):
    return f"{msg}, {name}!"

print(greet("Alice"))
print(greet("Bob", "Good morning"))
print(greet(msg="Hi there", name="Charlie"))