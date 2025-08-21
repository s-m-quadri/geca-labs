# Create a list of 5 integers.
# Print the first, middle, and last elements.
# Modify the third element to be 100, then print the entire list.

# 💡 TIP:
# Use indexing like list[0], list[-1], and list[2] to access or change values.

nums = [10, 20, 30, 40, 50]
print("First:", nums[0])
print("Middle:", nums[len(nums)//2])
print("Last:", nums[-1])
nums[2] = 100
print("Modified list:", nums)
