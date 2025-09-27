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
def compare(a, b):
    """
    Custom comparison:
    - Higher score comes first
    - If scores equal, alphabetical order of names
    """
    if a[1] > b[1]:
        return True
    elif a[1] < b[1]:
        return False
    else:
        return a[0] < b[0]  # tie-break by name (ascending)


def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Remaining elements
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


# Example usage
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 92)]
sorted_students = merge_sort(students)
print(sorted_students)
