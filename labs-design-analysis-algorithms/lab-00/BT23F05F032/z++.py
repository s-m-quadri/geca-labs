
full_name = input("Enter your full name: ")


lowercase_name = full_name.lower()
print("Lowercase:", lowercase_name)


uppercase_name = full_name.upper()
print("Uppercase:", uppercase_name)


parts = full_name.split()
initials = ". ".join([p[0].upper() for p in parts]) + "."
print("Initials:", initials)
