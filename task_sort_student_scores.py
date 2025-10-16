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
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 92)]

def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        # Compare scores (descending)
        if left[i][1] > right[j][1]:
            merged.append(left[i])
            i += 1
        elif left[i][1] < right[j][1]:
            merged.append(right[j])
            j += 1
        else:
            # If scores are equal, compare names (ascending)
            if left[i][0] < right[j][0]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

sorted_students = merge_sort(students)
print(sorted_students)
