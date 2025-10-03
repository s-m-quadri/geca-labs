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

def merge_sort(students):
    # Base case
    if len(students) <= 1:
        return students

    # Split the list into two halves
    mid = len(students) // 2
    left_half = merge_sort(students[:mid])
    right_half = merge_sort(students[mid:])

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    sorted_list = []
    i = j = 0

    # Merge two sorted lists with custom comparison
    while i < len(left) and j < len(right):
        name1, score1 = left[i]
        name2, score2 = right[j]

        # First compare scores (descending)
        if score1 > score2:
            sorted_list.append(left[i])
            i += 1
        elif score1 < score2:
            sorted_list.append(right[j])
            j += 1
        else:
            # Scores are equal, compare names (ascending)
            if name1 < name2:
                sorted_list.append(left[i])
                i += 1
            else:
                sorted_list.append(right[j])
                j += 1

    # Append any remaining elements
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    
    return sorted_list

# Example usage
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 92)]
sorted_students = merge_sort(students)
print(sorted_students)
