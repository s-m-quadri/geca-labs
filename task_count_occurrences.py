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

def count_inversions(arr):
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr, 0

        mid = len(arr) // 2
        left, left_inv = merge_sort(arr[:mid])
        right, right_inv = merge_sort(arr[mid:])
        merged, merge_inv = merge(left, right)

        return merged, left_inv + right_inv + merge_inv

    def merge(left, right):
        i = j = inv_count = 0
        merged = []

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
                # All remaining elements in left[i:] form inversions with right[j]
                inv_count += len(left) - i

        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, inv_count

    _, total_inversions = merge_sort(arr)
    return total_inversions


arr = [2, 4, 1, 3, 5]
print("Number of inversions:", count_inversions(arr))  # Output: 3



