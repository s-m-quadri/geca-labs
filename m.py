# Create a set of numbers with some duplicates.
# Show that only unique items remain.
# Add a new number and print the updated set.

# 💡 TIP:
# Sets remove duplicates automatically. Use `.add()` to insert.

numbers = {10, 20, 20, 30, 40, 40, 50}

print("Unique items in set:", numbers)

numbers.add(60)

print("Updated set:", numbers)
