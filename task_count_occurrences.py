# Puzzle / Learning focus:
# - You have a sorted array with repeated elements.
# - Count how many times a target number appears using binary search logic.
# - Consider how to find the first and last occurrence efficiently.
#
# Example test cases:
# Input: arr = [1, 2, 2, 2, 3, 4], target = 2
# Output: 3
#
# Input: arr = [5, 5, 5, 5, 5], target = 5
# Output: 5
def find_first(arr, target):
    low, high = 0, len(arr) - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            result = mid
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return result

def find_last(arr, target):
    low, high = 0, len(arr) - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            result = mid
            low = mid + 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return result

def count_occurrences(arr, target):
    first_index = find_first(arr, target)
    if first_index == -1:
        return 0
    last_index = find_last(arr, target)
    return last_index - first_index + 1

# Example test cases
arr1 = [1, 2, 2, 2, 3, 4]
target1 = 2
print(f"Input: arr = {arr1}, target = {target1}")
print(f"Output: {count_occurrences(arr1, target1)}")

print("-" * 20)

arr2 = [5, 5, 5, 5, 5]
target2 = 5
print(f"Input: arr = {arr2}, target = {target2}")
print(f"Output: {count_occurrences(arr2, target2)}")

print("-" * 20)

arr3 = [1, 2, 3, 4, 5]
target3 = 6
print(f"Input: arr = {arr3}, target = {target3}")
print(f"Output: {count_occurrences(arr3, target3)}")