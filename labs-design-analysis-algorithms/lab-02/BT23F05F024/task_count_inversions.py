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
def merge_and_count(arr, temp, left, mid, right):
    """Merge two sorted halves and count inversions."""
    i = left    
    j = mid + 1
    k = left    
    inv_count = 0

  
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
           
            temp[k] = arr[j]
            inv_count += (mid - i + 1)
            j += 1
        k += 1

  
    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1

   
    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1

    
    for i in range(left, right + 1):
        arr[i] = temp[i]

    return inv_count

def merge_sort_and_count(arr, temp, left, right):
    """Modified merge sort to count inversions."""
    inv_count = 0
    if left < right:
        mid = (left + right) // 2

        inv_count += merge_sort_and_count(arr, temp, left, mid)
        inv_count += merge_sort_and_count(arr, temp, mid + 1, right)
        inv_count += merge_and_count(arr, temp, left, mid, right)

    return inv_count

def count_inversions(arr):
    """Count inversions in the array using modified merge sort."""
    temp = [0] * len(arr)
    arr_copy = arr.copy()  # Don't modify the original array
    return merge_sort_and_count(arr_copy, temp, 0, len(arr) - 1)

if __name__ == "__main__":
    # Test case from the example
    test_arr = [2, 4, 1, 3, 5]
    print("Array:", test_arr)
    inversions = count_inversions(test_arr)
    print("Number of inversions:", inversions)
    print("Expected: 3 (inversions: (2,1), (4,1), (4,3))")

    # Additional test cases
    print("\nAdditional test cases:")

    # Already sorted array (no inversions)
    test_arr2 = [1, 2, 3, 4, 5]
    print("Array:", test_arr2)
    print("Inversions:", count_inversions(test_arr2))
    print("Expected: 0")

    # Reverse sorted array (maximum inversions)
    test_arr3 = [5, 4, 3, 2, 1]
    print("Array:", test_arr3)
    print("Inversions:", count_inversions(test_arr3))
    print("Expected: 10")

    # Array with duplicates
    test_arr4 = [3, 1, 3, 1]
    print("Array:", test_arr4)
    print("Inversions:", count_inversions(test_arr4))
    print("Expected: 3 (inversions: (3,1) at positions (0,1), (0,3), (2,3))")