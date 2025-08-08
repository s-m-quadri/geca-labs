# Create a set of numbers with some duplicates.
# Show that only unique items remain.
# Add a new number and print the updated set.

# 💡 TIP:
# Sets remove duplicates automatically. Use `.add()` to insert.

numbers = {1, 2, 3, 3, 4, 5, 2}
print("Only Unique items will remain: ",numbers)
numbers.add(6)
print("Updated set: ", numbers)