# Ask for a full name and display:
#  - All lowercase
#  - All uppercase
#  - Only initials (e.g., A. B. C.)

# 💡 TIP:
# Use `.split()` and `.upper()` / `.lower()`

full_name = input("Enter full name: ")
print(full_name.lower())
print(full_name.upper())
initials = [part[0].upper() + "." for part in full_name.split()]
print(" ".join(initials))