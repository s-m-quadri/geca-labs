# Puzzle / Learning focus:
# - Given a sorted array of positive numbers, find the smallest missing positive integer.
# - Use binary search thinking to locate the “gap” without checking every element.
# - Challenge: handle edge cases at the start and end of the array.
def smallest_missing(arr):
    n = len(arr)
    low, high = 0, n - 1
    mid = (low + high) // 2

    if arr[mid] == mid + 1:
        low = mid + 1
    else :
        high = mid - 1

    return low + 1
# Example test cases:
arr = [1, 2, 3, 5, 6]
print(smallest_missing(arr))
# Output: 4
arr = [2, 3, 4, 5]
print(smallest_missing(arr))
# Output: 1