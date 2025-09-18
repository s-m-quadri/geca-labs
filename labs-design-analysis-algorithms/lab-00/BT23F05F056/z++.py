# Ask for a full name and display:
#  - All lowercase
#  - All uppercase
#  - Only initials (e.g., A. B. C.)

# 💡 TIP:
# Use `.split()` and `.upper()` / `.lower()`
# Asking for full name
full_name = input("Enter your full name: ")

# Display all lowercase
print("Lowercase:", full_name.lower())

# Display all uppercase
print("Uppercase:", full_name.upper())

# Display initials
words = full_name.split()
initials = ""
for word in words:
    initials += word[0].upper() + ". "
print("Initials:", initials.strip())
