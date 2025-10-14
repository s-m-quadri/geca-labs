# Take full name input
name = input("Enter full name: ")

# Lowercase
print("Lower:", name.lower())

# Uppercase
print("Upper:", name.upper())

# Initials
parts = name.split()
initials = '. '.join(p[0].upper() for p in parts) + '.'
print("Initials:", initials)
