# binary_search_demo_visual.py
#
# Illustration: Represent the search space as a visual slice
# Focus: Show the part of the array being considered at each step


def binary_search_visual(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        print(f"Searching in {arr[low:high+1]}")
        mid = (low + high) // 2
        if arr[mid] == target:
            print(f"Found {target} at index {mid}")
            return mid
        elif target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    print(f"{target} not found")
    return -1

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7]
target = 4
binary_search_visual(arr, target)

print("\nAnother example:")
arr2 = [10, 20, 30, 40, 50]
target2 = 35
binary_search_visual(arr2, target2)
