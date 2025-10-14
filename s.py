
try:
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    
    result = x / y
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

except ValueError:
    print("Error: Please enter valid integers!")
