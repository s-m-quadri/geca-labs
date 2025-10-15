# Defining the function with a default message
def greet(name, msg="Hello"):
    print(msg, name)

greet("Alice")                  # Using default message
greet("Bob", "Good morning")    # Providing a custom message
greet(name="Charlie", msg="Hi") # Using named arguments
