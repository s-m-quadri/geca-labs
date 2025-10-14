# Function with default parameter
def greet(name, msg="Hello"):
    print(f"{msg}, {name}!")

# Call with only name (uses default message)
greet("Alice")

# Call with name and custom message
greet("Bob", "Hi")

# Call using named arguments
greet(name="Charlie", msg="Welcome")
