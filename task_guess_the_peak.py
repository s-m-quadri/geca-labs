def find_peak_mountain(arr):
    low, high = 0, len(arr) - 1
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < arr[mid + 1]:
            low = mid + 1
        else:
            high = mid
    return arr[low]

print(find_peak_mountain([1, 3, 7, 12, 9, 5, 2]))
print(find_peak_mountain([0, 2, 4, 6, 3, 1]))

