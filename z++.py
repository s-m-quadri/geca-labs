# Ask for a full name and display:
#  - All lowercase
#  - All uppercase
#  - Only initials (e.g., A. B. C.)

# 💡 TIP:
# Use `.split()` and `.upper()` / `.lower()`# Ask for a full name
full_name = input("Enter your full name: ")

# All lowercase
print("Lowercase:", full_name.lower())

# All uppercase
print("Uppercase:", full_name.upper())

# Only initials
parts = full_name.split()
initials = ""
for part in parts:
    initials += part[0].upper() + ". "
print("Initials:", initials.strip())


