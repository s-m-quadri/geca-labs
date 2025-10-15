# Create a set of numbers with some duplicates.
# Show that only unique items remain.
# Add a new number and print the updated set.

# 💡 TIP:
# Sets remove duplicates automatically. Use `.add()` to insert.


# Create a set with duplicates
numbers = {1, 2, 2, 3, 4, 4, 5}

# Print the set (duplicates removed automatically)
print("Unique numbers:", numbers)

# Add a new number
numbers.add(6)

# Print the updated set
print("Updated set:", numbers)
