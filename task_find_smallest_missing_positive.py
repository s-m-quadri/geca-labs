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
def find_smallest_missing(arr):
    left, right = 0, len(arr) - 1

    # If first number is not 1, smallest missing is 1
    if arr[0] != 1:
        return 1

    while left <= right:
        mid = (left + right) // 2

        # If the value matches its position (value = index + 1),
        # then the missing number is on the right side
        if arr[mid] == mid + 1:
            left = mid + 1
        else:
            right = mid - 1

    # The smallest missing number will be left + 1
    return left + 1


# Test cases
print(find_smallest_missing([1, 2, 3, 5, 6]))  # Output: 4
print(find_smallest_missing([2, 3, 4, 5]))     # Output: 1
print(find_smallest_missing([1, 2, 3, 4, 5]))  # Output: 6
print(find_smallest_missing([1]))              # Output: 2
