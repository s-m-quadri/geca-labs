# Create a set of numbers with some duplicates.
# Show that only unique items remain.
# Add a new number and print the updated set.

# 💡 TIP:
# Sets remove duplicates automatically. Use `.add()` to insert.
numbers = {1, 2, 3, 2, 4, 1, 5}
print(f"Set with duplicates removed: {numbers}")

numbers.add(6)
print(f"Updated set: {numbers}")