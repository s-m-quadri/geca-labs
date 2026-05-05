# Ask for a full name and display:
#  - All lowercase
#  - All uppercase
#  - Only initials (e.g., A. B. C.)

# 💡 TIP:
# Use `.split()` and `.upper()` / `.lower()`
# Ask for a full name and display:
#  - All lowercase
#  - All uppercase
#  - Only initials (e.g., A. B. C.)

# 💡 TIP:
# Use `.split()` and `.upper()` / `.lower()`

full_name = input("Enter your full name: ")

print("Lowercase:", full_name.lower())
print("Uppercase:", full_name.upper())

# Only initials
initials = ". ".join([part[0].upper() for part in full_name.split()]) + "."
print("Initials:", initials)