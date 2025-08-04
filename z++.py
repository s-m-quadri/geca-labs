# Ask for a full name and display:
#  - All lowercase
#  - All uppercase
#  - Only initials (e.g., A. B. C.)

# 💡 TIP:
# Use `.split()` and `.upper()` / `.lower()`
full_name = input("Enter your full name: ")

print(full_name.lower())
print(full_name.upper())

parts = full_name.split()
initials = [p[0].upper() + '.' for p in parts]
print(' '.join(initials))
