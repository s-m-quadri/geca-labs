# Ask for a full name and display:
#  - All lowercase
#  - All uppercase
#  - Only initials (e.g., A. B. C.)

# 💡 TIP:
# Use `.split()` and `.upper()` / `.lower()`def name_formats():
def name_formats():
    full_name = input("Enter your full name: ")
    print("Lowercase:", full_name.lower())
    print("Uppercase:", full_name.upper())
    initials = " ".join([word[0].upper() + "." for word in full_name.split()])
    print("Initials:", initials)

name_formats()
