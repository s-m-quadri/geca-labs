# Ask for a full name and display:
#  - All lowercase
#  - All uppercase
#  - Only initials (e.g., A. B. C.)

# 💡 TIP:
# Use `.split()` and `.upper()` / `.lower()`
full_name = input("Enter your full name: ")

lowercase = full_name.lower()
uppercase = full_name.upper()
initials = '.'.join([part[0].upper() for part in full_name.split()]) + '.'

print("All lowercase:", lowercase)
print("All uppercase:", uppercase)
print("Initials:", initials)
