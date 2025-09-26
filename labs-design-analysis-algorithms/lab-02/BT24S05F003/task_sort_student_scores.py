# Given a list of tuples containing student names and scores:
# students = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 92)]
# Sort them in:
#     - Descending order of scores
#     - If scores are equal, ascending alphabetical order by name

# Expected Output:
# [("Bob", 92), ("David", 92), ("Alice", 85), ("Charlie", 78)]

# INSTRUCTIONS:
# - Implement merge sort to achieve the required sorting order.
# - Modify the comparison logic inside merge function accordingly.
# - Do not use Python's built-in sort().

# Write your solution here

def count_inversion_pairs(arr):
    inversion_pairs = []

    def merge_sort(arr, left_index=0):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = merge_sort(arr[:mid], left_index)
        right = merge_sort(arr[mid:], left_index + mid)
        return merge(left, right, left_index, mid)

    def merge(left, right, left_index, mid):
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                # Record all inversions: left[i:] with right[j]
                for k in range(i, len(left)):
                    inversion_pairs.append((left_index + k, left_index + mid + j))
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    merge_sort(arr)
    return len(inversion_pairs), inversion_pairs


# Test case
arr = [2, 4, 1, 3, 5]
count, pairs = count_inversion_pairs(arr)
print("Number of inversions:", count)
print("Inversion pairs (i,j):", pairs)

