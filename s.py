try:
    x = int(input("Enter the numerator: "))
    y = int(input("Enter the denominator: "))
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Please enter valid integers!")
else:
    print(f"Result: {result}")
