# Ask for a full name and display:
#  - All lowercase
#  - All uppercase
#  - Only initials (e.g., A. B. C.)

# 💡 TIP:
# Use `.split()` and `.upper()` / `.lower()`

name = input("Enter your full name: ")

print(f"Lowercase: {name.lower()}")
print(f"Uppercase: {name.upper()}")

initials = [word[0].upper() + "." for word in name.split()]
print(f"Initials: {' '.join(initials)}")