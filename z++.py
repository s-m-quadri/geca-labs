# Ask for a full name and display:
#  - All lowercase
#  - All uppercase
#  - Only initials (e.g., A. B. C.)

# 💡 TIP:
# Use `.split()` and `.upper()` / `.lower()`
# Ask for full name
name = input("Enter your full name: ")

# Display all lowercase
print("Lowercase:", name.lower())

# Display all uppercase
print("Uppercase:", name.upper())

# Display initials (e.g., A. B. C.)
parts = name.split()
initials = ". ".join([p[0].upper() for p in parts]) + "."
print("Initials:", initials)
