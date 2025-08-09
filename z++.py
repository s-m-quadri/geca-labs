# Ask for a full name and display:
#  - All lowercase
#  - All uppercase
#  - Only initials (e.g., A. B. C.)

# 💡 TIP:
# Use `.split()` and `.upper()` / `.lower()`

name = input("Enter your full name: ")

print(name.lower())
print(name.upper())

part = name.split(" ")

for i in range(len(part)):
    print(f"{part[i][0].upper()}. ",end="")

print()