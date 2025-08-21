# Create a set of numbers with some duplicates.
# Show that only unique items remain.
# Add a new number and print the updated set.

# 💡 TIP:
# Sets remove duplicates automatically. Use `.add()` to insert.

numbers = {1, 2, 3, 2, 4, 5, 3, 6, 1}

print("Original set (duplicates removed):", numbers)

numbers.add(7)

print("Updated set after adding 7:", numbers)