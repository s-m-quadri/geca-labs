def smallest_missing_positive(arr):
    low, high = 0, len(arr) - 1

    # If 1 is missing at the start
    if arr[0] != 1:
        return 1

    while low <= high:
        mid = (low + high) // 2

        # If the element matches its "ideal" position, move right
        if arr[mid] == mid + 1:
            low = mid + 1
        else:
            high = mid - 1

    # When loop ends, low points to the first missing position
    return low + 1


# Example test cases
print(smallest_missing_positive([1, 2, 3, 5, 6]))  # Output: 4
print(smallest_missing_positive([2, 3, 4, 5]))     # Output: 1
print(smallest_missing_positive([1, 2, 3, 4, 5]))  # Output: 6
