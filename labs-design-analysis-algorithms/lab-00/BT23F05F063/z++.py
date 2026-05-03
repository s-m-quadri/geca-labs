# Ask for a full name and display:
#  - All lowercase
#  - All uppercase
#  - Only initials (e.g., A. B. C.)

# 💡 TIP:
# Use `.split()` and `.upper()` / `.lower()`

# Get full name from user
full_name = input("Enter your full name: ")

# Print in lowercase
print(f"Lowercase: {full_name.lower()}")

# Print in uppercase
print(f"Uppercase: {full_name.upper()}")

# Get initials
names = full_name.split()
initials = '. '.join(name[0].upper() for name in names) + '.'
print(f"Initials: {initials}")