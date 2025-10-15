def count_occurrences(arr, target):
    def find_first(arr, target):
        low, high, first = 0, len(arr) - 1, -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                first = mid
                high = mid - 1
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return first

    def find_last(arr, target):
        low, high, last = 0, len(arr) - 1, -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                last = mid
                low = mid + 1
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return last

    first = find_first(arr, target)
    last = find_last(arr, target)
    return 0 if first == -1 else last - first + 1

arr = [1, 2, 2, 2, 3, 4]
print(count_occurrences(arr, 2))
arr = [5, 5, 5, 5, 5]
print(count_occurrences(arr, 5))
