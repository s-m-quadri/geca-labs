# Create a set of numbers with some duplicates.
# Show that only unique items remain.
# Add a new number and print the updated set.

# 💡 TIP:
# Sets remove duplicates automatically. Use `.add()` to insert.

# Create a set with duplicates
numbers = {1, 2, 2, 3, 4, 4, 5}

# Print the set to show only unique items remain
print(numbers)  # Output will be {1, 2, 3, 4, 5}

# Add a new number
numbers.add(6)

# Print the updated set
print(numbers)
