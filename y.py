# Take user input
num = input("Enter a number: ")

# Check if it's a valid integer
if num.isdigit():
    print("You entered:", int(num))
else:
    print("Invalid input")
