# Given an array of integers, count the number of inversions in the array.
# An inversion is a pair (i, j) such that i < j and arr[i] > arr[j].

# Example:
# Input: [2, 4, 1, 3, 5]
# Output: 3
# Explanation: The inversions are (2,1), (4,1), (4,3)

# INSTRUCTIONS:
# - Implement a function using Merge Sort modification to count inversions efficiently.
# - Target time complexity: O(n log n)
# - Do not use brute force O(n^2) method.

# Write your solution here

def merge_and_count(arr, temp_arr, left, mid, right):
    """Merge two sorted halves and count inversions."""
    i, j, k = left, mid + 1, left
    inv_count = 0
    
    # Merge the two halves while counting inversions
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            # arr[i] > arr[j], so there are (mid - i + 1) inversions
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)
            j += 1
        k += 1
    
    # Copy remaining elements
    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1
    
    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1
    
    # Copy back the merged elements to original array
    for i in range(left, right + 1):
        arr[i] = temp_arr[i]
    
    return inv_count

def merge_sort_and_count(arr, temp_arr, left, right):
    """Recursive merge sort that counts inversions."""
    inv_count = 0
    if left < right:
        mid = (left + right) // 2
        
        inv_count += merge_sort_and_count(arr, temp_arr, left, mid)
        inv_count += merge_sort_and_count(arr, temp_arr, mid + 1, right)
        inv_count += merge_and_count(arr, temp_arr, left, mid, right)
    
    return inv_count

def count_inversions(arr):
    """Count inversions in array using modified merge sort."""
    temp_arr = [0] * len(arr)
    arr_copy = arr.copy()  # Don't modify original array
    return merge_sort_and_count(arr_copy, temp_arr, 0, len(arr) - 1)

# Test the function
if __name__ == "__main__":
    # Test case 1
    test_arr1 = [2, 4, 1, 3, 5]
    result1 = count_inversions(test_arr1)
    print(f"Array: {test_arr1}")
    print(f"Number of inversions: {result1}")
    print(f"Expected: 3")
    print()
    
    # Test case 2
    test_arr2 = [5, 4, 3, 2, 1]
    result2 = count_inversions(test_arr2)
    print(f"Array: {test_arr2}")
    print(f"Number of inversions: {result2}")
    print(f"Expected: 10")
    print()
    
    # Test case 3
    test_arr3 = [1, 2, 3, 4, 5]
    result3 = count_inversions(test_arr3)
    print(f"Array: {test_arr3}")
    print(f"Number of inversions: {result3}")
    print(f"Expected: 0")
