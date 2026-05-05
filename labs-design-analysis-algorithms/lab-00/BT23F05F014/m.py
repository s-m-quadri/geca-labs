# Create a set of numbers with some duplicates.
# Show that only unique items remain.
# Add a new number and print the updated set.

# 💡 TIP:
# Sets remove duplicates automatically. Use `.add()` to insert.
#code
numbers = {1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 9}
print("Unique numbers:", numbers)
numbers.add(10)
print("Updated numbers:", numbers)
