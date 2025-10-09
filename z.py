# Combine everything you've learned.
# Ask user for a number, check if it's even, calculate its square root,
# and print a random motivational quote if the number is > 10.

# 💡 TIP:
# Combine `if`, `math`, `random`, and type conversion.
#code
import math
import random


# List of motivational quotes
quotes = [
    "Believe you can and you're halfway there.",
    "Your limitation—it's only your imagination.",
    "Push yourself, because no one else is going to do it for you.",
    "Great things never come from comfort zones.",
    "Dream it. Wish it. Do it.",
    "Success doesn't just find you. You have to go out and get it.",
    "The harder you work for something, the greater you'll feel when you achieve it.",
    "Don't watch the clock; do what it does. Keep going.",
    "Little things make big days.",
    "It's going to be hard, but hard does not mean impossible."
]   
# Function to get a valid number from the user
def get_number():

    while True:
        try:
            num = float(input("Enter a number: "))
            return num
        except ValueError:
            print("That's not a valid number. Please try again.")   
# Main function
def main():
    number = get_number()

    # Check if the number is even or odd
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

    # Calculate and print the square root
    if number >= 0:
        sqrt = math.sqrt(number)
        print(f"The square root of {number} is {sqrt}.")
    else:
        print("Cannot calculate the square root of a negative number.")

    # Print a random motivational quote if the number is greater than 10
    if number > 10:
        quote = random.choice(quotes)
        print("Motivational Quote: " + quote)
# Run the main function
if __name__ == "__main__":
    main()