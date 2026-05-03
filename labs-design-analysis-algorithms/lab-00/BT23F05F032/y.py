user_input = input("Enter a number: ")

if user_input.isdigit() or (user_input.startswith('-') and user_input[1:].isdigit()):
    number = int(user_input)
    print("Valid integer:", number)
else:
    print("Invalid input")
