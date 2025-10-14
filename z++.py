# Ask for a full name and display:
#  - All lowercase
#  - All uppercase
#  - Only initials (e.g., A. B. C.)

# 💡 TIP:
# Use `.split()` and `.upper()` / `.lower()`
full_name = input("Enter your full name: ")

print("Lowercase:", full_name.lower())
print("Uppercase:", full_name.upper())

names = full_name.split()
initials = ""
for name in names:
    if name:  
        initials += name[0].upper() + ". "
print("Initials:", initials.strip())