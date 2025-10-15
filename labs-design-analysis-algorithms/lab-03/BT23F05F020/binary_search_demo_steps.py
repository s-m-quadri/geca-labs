# binary_search_demo_steps.py
# Illustration: Watch binary search narrow down step by step
# Focus: Track low, high, and mid values as the algorithm searches

def binary_search_iterative_steps(arr, target):
    low, high = 0, len(arr) - 1
    step = 1
    while low <= high:
        mid = (low + high) // 2
        print(f"Step {step}: low={low}, high={high}, mid={mid}, arr[mid]={arr[mid]}")
        if arr[mid] == target:
            print(f"Found {target} at index {mid}")
            return mid
        elif target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
        step += 1
    print(f"{target} not found")
    return -1
#todo
# Example usage
arr = [1, 3, 5, 7, 9, 11]
target = 7
binary_search_iterative_steps(arr, target)

print("\nAnother example:")
arr2 = [2, 4, 6, 8, 10]
target2 = 5
binary_search_iterative_steps(arr2, target2)
