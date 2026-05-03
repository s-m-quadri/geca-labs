# Ask for a full name and display:
#  - All lowercase
#  - All uppercase
#  - Only initials (e.g., A. B. C.)

# 💡 TIP:
# Use `.split()` and `.upper()` / `.lower()`

full_name = input("Enter your full name: ")
lower_name = full_name.lower()
upper_name = full_name.upper()
initials = ''.join([name[0].upper() + '.' for name in full_name.split()])

print("Lowercase:", lower_name)
print("Uppercase:", upper_name)
print("Initialls:", initials)