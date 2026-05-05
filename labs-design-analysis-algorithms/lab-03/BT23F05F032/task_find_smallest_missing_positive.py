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
# Function to find the smallest missing positive integer in a sorted array
def smallest_missing(arr):
    """
    Returns the smallest missing positive integer in a sorted array of positive numbers.
    Uses binary search approach: O(log n)
    """
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == mid + 1:
            # Left part is perfect, move right
            low = mid + 1
        else:
            # Mismatch found, missing number is here or before
            high = mid - 1

    # When loop ends, low points to the first mismatch
    return low + 1


# --------------------------
# Example Test Cases
# --------------------------
print(smallest_missing([1, 2, 3, 5, 6]))   # Output: 4
print(smallest_missing([2, 3, 4, 5]))      # Output: 1
print(smallest_missing([1, 2, 3, 4, 5]))   # Output: 6
print(smallest_missing([1, 3, 4, 5, 6]))   # Output: 2
print(smallest_missing([]))                # Output: 1
