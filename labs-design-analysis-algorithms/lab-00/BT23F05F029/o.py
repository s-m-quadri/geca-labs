# Create a function `greet` that takes a name and an optional message.
#  - If no message is provided, it should default to "Hello".
#  - Call the function in three different ways using default and named arguments.

# 💡 TIP:
#  Use `def greet(name, msg="Hello"):` to set a default value.

# Define the function with a default message
def greet(name, msg="Hello"):
    print(f"{msg}, {name}!")

# Call the function in three different ways
greet("Rama")                          # using default message
greet("Aarav", "Good morning")         # providing a custom message
greet(name="Isha", msg="Welcome")      # using named arguments
