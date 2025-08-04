# Ask for a full name and display:
#  - All lowercase
#  - All uppercase
#  - Only initials (e.g., A. B. C.)

# 💡 TIP:
# Use `.split()` and `.upper()` / `.lower()`


Fullname = input("Enter your full name: ")

print("Lowercase:", Fullname.lower())
print("Uppercase:", Fullname.upper())

initials = ". ".join([word[0].upper() for word in Fullname.split()]) + "."
print("Initials:", initials)