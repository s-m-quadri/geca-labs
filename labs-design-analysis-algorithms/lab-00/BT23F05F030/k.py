# Create a tuple of 3 items.
# Try to modify the second item and observe the error.
# Print each item in the tuple using a loop.

# 💡 TIP:
# Tuples are like lists, but immutable (they cannot be changed).
tuple = ("apple","ball","cat")
#tuple[1]="doll" #typeerror
for i in tuple:
    print(i)