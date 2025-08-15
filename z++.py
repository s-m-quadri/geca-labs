# Ask for a full name and display:
#  - All lowercase
#  - All uppercase
#  - Only initials (e.g., A. B. C.)

# 💡 TIP:
# Use `.split()` and `.upper()` / `.lower()`

name = input("Enter full name: ")
print("LowerCase:", name.lower())
print("UpperCase:", name.upper())
print("Initials:", name[0],".")