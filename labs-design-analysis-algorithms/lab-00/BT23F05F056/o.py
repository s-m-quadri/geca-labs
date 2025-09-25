# Create a function `greet` that takes a name and an optional message.
#  - If no message is provided, it should default to "Hello".
#  - Call the function in three different ways using default and named arguments.

# 💡 TIP:
#  Use `def greet(name, msg="Hello"):` to set a default value.
# Defining the greet function
def greet(name, msg="Hello"):
    print(msg, name)

# Calling the function in different ways
greet("Isha")                     # uses default message
greet("Aarav", "Good morning")    # custom message
greet(name="Meera", msg="Welcome") # using named arguments
