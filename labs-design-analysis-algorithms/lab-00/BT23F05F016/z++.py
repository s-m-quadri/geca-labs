# Asking user for full name
full_name = input("Enter your full name: ")

# Display all lowercase
print("Lowercase:", full_name.lower())

# Display all uppercase
print("Uppercase:", full_name.upper())


words = full_name.split()
initials = [word[0].upper() + "." for word in words]
print("Initials:", " ".join(initials))
