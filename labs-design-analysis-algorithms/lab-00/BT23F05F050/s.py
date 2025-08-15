# Take two numbers from the user and divide them.
#  - Handle divide-by-zero errors using try-except.
#  - Also handle non-integer input using `try` and `ValueError`.

# 💡 TIP:
# Use `except ZeroDivisionError:` and `except ValueError:` blocks.
try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    
   
    result = a / b
    print(f"Result: {result}")

except ValueError:
    print("Invalid input! Please enter integers only.")

except ZeroDivisionError:
    print("Error! Cannot divide by zero.")
