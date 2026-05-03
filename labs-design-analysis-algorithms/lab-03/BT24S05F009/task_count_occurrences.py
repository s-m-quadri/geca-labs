# Puzzle / Learning focus:
# - You have a sorted array with repeated elements.
# - Count how many times a target number appears using binary search logic.
# - Consider how to find the first and last occurrence efficiently.
def count_occurrences(arr, target):
    n = len(arr)

    def first_occurrences():
        low, high, first = 0, n-1, -1
        while low <= high:
            mid = (low + high) // 2
            if target == arr[mid]:
                first = mid
                high = mid - 1
            elif target < arr[mid]:
                high = mid - 1
            else :
                low = mid + 1
        return first

    def last_occurrences():
        low, high, last = 0, n-1, -1
        while low <= high:
            mid = (low + high) // 2
            if target == arr[mid]:
                last = mid
                low = mid + 1
            elif target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return last

    first = first_occurrences()
    last = last_occurrences()

    if first == -1:
        return 0
    return last - first + 1


# Example test cases:
arr = [1, 2, 2, 2, 3, 4]
target = 2
print(count_occurrences(arr,target))
# Output: 3

arr = [5, 5, 5, 5, 5]
target = 5
print(count_occurrences(arr,target))
# Output: 5
