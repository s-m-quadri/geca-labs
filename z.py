# Combine everything you've learned.
# Ask user for a number, check if it's even, calculate its square root,
# and print a random motivational quote if the number is > 10.

# 💡 TIP:
# Combine `if`, `math`, `random`, and type conversion.

motivational_quotes = [
    "Mehnat itni khamoshi se karo ke kamyabi shor macha de.",
    "Jab tak thakoge nahi, tab tak rukna mat.",
    "Asli hero wahi hota hai jo girke bhi khud uthta hai.",
    "Sapne woh nahi jo neend mein aate hain, sapne woh hain jo neend nahi aane dete.",
    "Kamyabi ka maza tab hi aata hai jab sab tumhe haarte dekhna chahein.",
    "Aaj ka dard kal ki taqat banega.",
    "Soch ko badlo, sitare khud-b-khud badlenge.",
    "Zindagi jeetne ke liye ek jazbe ki zarurat hoti hai.",
    "Raste kabhi khud nahi bante, unhe banana padta hai.",
    "Koshish karne walon ki kabhi haar nahi hoti."
]
import random

num=int(input("Enter a number: "))

if num%2==0:
    print(num**2)
    if num>10:
        print(random.choice(motivational_quotes))