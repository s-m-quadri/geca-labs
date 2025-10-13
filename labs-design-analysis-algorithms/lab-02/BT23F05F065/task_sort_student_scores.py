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


def merge(students, left, mid, right):
    L = students[left:mid+1]
    R = students[mid+1:right+1]

    i, j, k = 0, 0, left

    while i < len(L) and j < len(R):
        # Sort by score (descending), then by name (ascending)
        if L[i][1] > R[j][1] or (L[i][1] == R[j][1] and L[i][0] < R[j][0]):
            students[k] = L[i]
            i += 1
        else:
            students[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        students[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        students[k] = R[j]
        j += 1
        k += 1


def merge_sort(students, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(students, left, mid)
        merge_sort(students, mid + 1, right)
        merge(students, left, mid, right)


# Example
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 92)]
merge_sort(students, 0, len(students) - 1)
print(students)
