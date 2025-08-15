# Ask for a full name and display:
#  - All lowercase
#  - All uppercase
#  - Only initials (e.g., A. B. C.)

# 💡 TIP:
# Use `.split()` and `.upper()` / `.lower()`

# Ask for full name
full_name = input("Enter your full name: ")

# Display all lowercase
print("Lowercase:", full_name.lower())

# Display all uppercase
print("Uppercase:", full_name.upper())

# Display only initials (e.g., A. B. C.)
initials = '. '.join([word[0].upper() for word in full_name.split()]) + '.'
print("Initials:", initials)
