# Take two numbers from the user and divide them.
#  - Handle divide-by-zero errors using try-except.
#  - Also handle non-integer input using `try` and `ValueError`.

# 💡 TIP:
# Use `except ZeroDivisionError:` and `except ValueError:` blocks.
try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    
    result = a / b

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Please enter valid integers.")
