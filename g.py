try:
    value = int(input("Enter number: "))
    print(f"You entered: {value}")
except ValueError:
    print("Invalid input! Please enter a number.")