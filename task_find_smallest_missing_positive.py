
def find_smallest_missing_positive(arr):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == mid + 1:
            low = mid + 1
        else:
            high = mid - 1
    return low + 1
