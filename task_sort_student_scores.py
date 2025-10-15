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
# -------------------------------------------
# TASK: Sort Students by Score (Descending) and Name (Ascending)
# Using Merge Sort
# -------------------------------------------

def merge_sort_students(students):
    # Base case
    if len(students) <= 1:
        return students

    mid = len(students) // 2
    left = merge_sort_students(students[:mid])
    right = merge_sort_students(students[mid:])
    return merge(left, right)


def merge(left, right):
    merged = []
    i = j = 0

    # Compare tuples based on custom logic
    while i < len(left) and j < len(right):
        name1, score1 = left[i]
        name2, score2 = right[j]

        # Sort by descending score
        if score1 > score2:
            merged.append(left[i])
            i += 1
        elif score1 < score2:
            merged.append(right[j])
            j += 1
        else:
            # If scores are equal, sort by ascending name
            if name1 < name2:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

    # Append remaining elements
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


# -------------------------------------------
# Example Usage
# -------------------------------------------
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 92)]

sorted_students = merge_sort_students(students)
print("Sorted Students:", sorted_students)
