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
def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        # Sort primarily by descending score, then ascending name
        if left[i][1] > right[j][1]:
            merged.append(left[i])
            i += 1
        elif left[i][1] < right[j][1]:
            merged.append(right[j])
            j += 1
        else:
            if left[i][0] < right[j][0]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged


def merge_sort(students):
    if len(students) <= 1:
        return students

    mid = len(students) // 2
    left = merge_sort(students[:mid])
    right = merge_sort(students[mid:])

    return merge(left, right)


students = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 92)]
print(merge_sort(students))
