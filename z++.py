# Ask for a full name and display:
#  - All lowercase
#  - All uppercase
#  - Only initials (e.g., A. B. C.)

# 💡 TIP:
# Use `.split()` and `.upper()` / `.lower()`
# Ask user for full name
full_name = input("Enter your full name: ")

# All lowercase
print("Lowercase:", full_name.lower())

# All uppercase
print("Uppercase:", full_name.upper())

# Initials
words = full_name.split()
initials = ". ".join([word[0].upper() for word in words]) + "."
print("Initials:", initials)
