# Recursive Merge Sort
def merge_sort_recursive(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort_recursive(arr[:mid])
    right = merge_sort_recursive(arr[mid:])
    return merge(left, right)
 
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
 
# Iterative (Bottom-Up) Merge Sort
def merge_sort_iterative(arr):
    width = 1
    n = len(arr)
    while width < n:
        for i in range(0, n, 2 * width):
            left = arr[i:i + width]
            right = arr[i + width:i + 2 * width]
            arr[i:i + 2 * width] = merge(left, right)
        width *= 2
    return arr
 
# Driver
arr = [38, 27, 43, 3, 9, 82, 10]
print("Recursive:", merge_sort_recursive(arr))
print("Iterative:", merge_sort_iterative(arr.copy()))
# Completed the program