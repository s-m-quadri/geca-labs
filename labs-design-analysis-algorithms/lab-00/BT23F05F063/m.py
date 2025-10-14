# Create a set of numbers with some duplicates.
# Show that only unique items remain.
# Add a new number and print the updated set.

# 💡 TIP:
# Sets remove duplicates automatically. Use `.add()` to insert.

numbers = {1, 2, 2, 3, 3, 3, 4, 4, 4, 4}
print(f"Set with duplicates removed: {numbers}")

numbers.add(5)
print(f"After adding 5: {numbers}")
