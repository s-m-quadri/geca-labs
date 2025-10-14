# Create a list of squares for numbers 1 to 10 using list comprehension.
#  - Also create a list of even numbers from 1 to 20.

# 💡 TIP:
# Format → `[expression for item in iterable if condition]`

# List of squares from 1 to 10
squares = [x**2 for x in range(1, 11)]
print("Squares:", squares)

# List of even numbers from 1 to 20
evens = [x for x in range(1, 21) if x % 2 == 0]
print("Even numbers:", evens)

