# Ask for a full name and display:
#  - All lowercase
#  - All uppercase
#  - Only initials (e.g., A. B. C.)

# 💡 TIP:
# Use `.split()` and `.upper()` / `.lower()`


name = input("Enter full name: ")
parts = name.split()
initials = '. '.join(p[0].upper() for p in parts) + '.'
print("Lower:", name.lower())
print("Upper:", name.upper())
print("Initials:", initials)