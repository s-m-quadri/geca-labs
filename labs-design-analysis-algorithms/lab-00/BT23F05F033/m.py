# Create a set of numbers with some duplicates.
# Show that only unique items remain.
# Add a new number and print the updated set.

# 💡 TIP:
# Sets remove duplicates automatically. Use `.add()` to insert.
# Create a set of numbers with some duplicates
numbers = {10, 20, 30, 20, 40, 30, 50}

# Show that only unique items remain
print("Unique numbers in the set:", numbers)

# Add a new number to the set
numbers.add(60)

# Print the updated set
print("Updated set after adding 60:", numbers)
