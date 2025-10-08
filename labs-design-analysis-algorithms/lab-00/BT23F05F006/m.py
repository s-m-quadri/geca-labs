# Create a set of numbers with some duplicates.
# Show that only unique items remain.
# Add a new number and print the updated set.

# 💡 TIP:
# Sets remove duplicates automatically. Use `.add()` to insert.

nums = {1,2,3,3,4,5,5,5,6,6}
print("Unique items:",nums)

nums.add(7)
print("after adding 7: ",nums)