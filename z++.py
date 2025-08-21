# Ask for a full name and display:
#  - All lowercase
#  - All uppercase
#  - Only initials (e.g., A. B. C.)

# 💡 TIP:
# Use `.split()` and `.upper()` / `.lower()`
name = input("Enter your full name: ")

print("Lowercase:", name.lower())
print("Uppercase:", name.upper())

initials = " ".join([part[0].upper() + "." for part in name.split()])
print("Initials:", initials)
