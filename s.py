# Take two numbers from the user and divide them.
#  - Handle divide-by-zero errors using try-except.
#  - Also handle non-integer input using `try` and `ValueError`.

# 💡 TIP:
# Use `except ZeroDivisionError:` and `except ValueError:` blocks.


    num1 = int(input("Enter the numerator: "))
    num2 = int(input("Enter the denominator: "))
    
    result = num1 / num2
    
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
    
except ValueError:
    print("Error: Please enter valid integers!")
    
else:
    print(f"Result: {result}")
