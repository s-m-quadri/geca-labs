# Ask for a full name and display:
#  - All lowercase
#  - All uppercase
#  - Only initials (e.g., A. B. C.)

# 💡 TIP:
# Use `.split()` and `.upper()` / `.lower()`

full_name = input("Enter your full name: ")

print(f"Lowercase: {full_name.lower()}")

print(f"Uppercase: {full_name.upper()}")

name_parts = full_name.split()
initials = ". ".join([part[0].upper() for part in name_parts]) + "."
print(f"Initials: {initials}")