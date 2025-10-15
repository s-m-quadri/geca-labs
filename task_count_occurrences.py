def count_occurrences(arr, target):
    def first_occurrence(arr, target):
        low, high = 0, len(arr) - 1
        first = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                first = mid
                high = mid - 1  # keep searching left
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return first

    def last_occurrence(arr, target):
        low, high = 0, len(arr) - 1
        last = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                last = mid
                low = mid + 1  # keep searching right
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return last

    first = first_occurrence(arr, target)
    last = last_occurrence(arr, target)

    if first == -1:
        return 0  # target not found
    return last - first + 1


# Example test cases
arr1 = [1, 2, 2, 2, 3, 4]
target1 = 2
print(count_occurrences(arr1, target1))  # Output: 3

arr2 = [5, 5, 5, 5, 5]
target2 = 5
print(count_occurrences(arr2, target2))  # Output: 5
