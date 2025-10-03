# Puzzle / Learning focus:
# - Given a sorted array of positive numbers, find the smallest missing positive integer.
# - Use binary search thinking to locate the “gap” without checking every element.
# - Challenge: handle edge cases at the start and end of the array.
#
# Example test cases:
# Input: [1, 2, 3, 5, 6]
# Output: 4
#
# Input: [2, 3, 4, 5]
# Output: 1

def find_smallest_missing_positive(nums):
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == mid + 1:
            low = mid + 1 # No missing number on the left
        else:
            high = mid - 1 # Missing number is on the left

    # At the end, `low` is the index where the mismatch starts
    return low + 1

print(find_smallest_missing_positive([1, 2, 3, 5, 6]))
print(find_smallest_missing_positive([2, 3, 4, 5]))