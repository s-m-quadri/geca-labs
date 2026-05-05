def find_peak(arr):
    """
    Return the peak element value in a mountain array.
    Assumes arr has at least 3 elements and contains a single peak (strictly increasing then strictly decreasing).
    """
    if not arr:
        raise ValueError("Array must not be empty")
    n = len(arr)
    if n == 1:
        return arr[0]
    low, high = 0, n - 1

    while low < high:
        mid = (low + high) // 2
        # Compare mid with mid+1
        if arr[mid] < arr[mid + 1]:
            # Rising slope: peak is to the right
            low = mid + 1
        else:
            # Falling slope (or mid is peak): peak is at mid or to the left
            high = mid
    # low == high is the peak index
    return arr[low]


# Example usage
print(find_peak([1, 3, 7, 12, 9, 5, 2]))  # Output: 12
print(find_peak([0, 2, 4, 6, 3, 1]))      # Output: 6
