def smallest_missing_positive(arr):
    if arr[0] != 1:
        return 1
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == mid + 1:
            low = mid + 1
        else:
            high = mid - 1
    return low + 1

print(smallest_missing_positive([1, 2, 3, 5, 6]))
print(smallest_missing_positive([2, 3, 4, 5]))

