# Create a function `greet` that takes a name and an optional message.
#  - If no message is provided, it should default to "Hello".
#  - Call the function in three different ways using default and named arguments.

# 💡 TIP:
#  Use `def greet(name, msg="Hello"):` to set a default value.

def greet(name, msg="Hello"):
    print(f"{msg} {name}")

greet("Rutik")
greet("Anita", "Good morning")
greet(name="Karan", msg="Hi")

