# Ask for a full name and display:
#  - All lowercase
#  - All uppercase
#  - Only initials (e.g., A. B. C.)

# 💡 TIP:
# Use `.split()` and `.upper()` / `.lower()`
# Ask for full name
full_name = input("Enter your full name: ")

# Lowercase
print("Lowercase:", full_name.lower())

# Uppercase
print("Uppercase:", full_name.upper())

# Only initials
parts = full_name.split()
initials = " ".join([p[0].upper() + "." for p in parts])
print("Initials:", initials)
