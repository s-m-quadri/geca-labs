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
def merge_sort_students(students):
    if len(students) <= 1:
        return students

    mid = len(students) // 2
    left = merge_sort_students(students[:mid])
    right = merge_sort_students(students[mid:])
    return merge(left, right)

def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        student_left = left[i]
        student_right = right[j]

        # Custom comparison logic:
        # 1. Higher score comes first
        # 2. If scores are equal, compare names (ascending)
        if student_left[1] > student_right[1]:
            merged.append(student_left)
            i += 1
        elif student_left[1] < student_right[1]:
            merged.append(student_right)
            j += 1
        else:
            # Scores equal: compare names alphabetically
            if student_left[0] < student_right[0]:
                merged.append(student_left)
                i += 1
            else:
                merged.append(student_right)
                j += 1

    # Append remaining items
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

# Example usage
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 92)]
sorted_students = merge_sort_students(students)
print(sorted_students)
