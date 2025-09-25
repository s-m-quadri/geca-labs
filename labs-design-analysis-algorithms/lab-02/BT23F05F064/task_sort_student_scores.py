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
    # Create temporary lists
    left_list = students[left:mid+1]
    right_list = students[mid+1:right+1]

    i = j = 0
    k = left
 
    # Merge with custom comparison logic
    while i < len(left_list) and j < len(right_list):
        # Compare based on score descending, then name ascending
        if (left_list[i][1] > right_list[j][1]) or \
           (left_list[i][1] == right_list[j][1] and left_list[i][0] < right_list[j][0]):
            students[k] = left_list[i]
            i += 1
        else:
            students[k] = right_list[j]
            j += 1
        k += 1

    # Copy remaining elements
    while i < len(left_list):
        students[k] = left_list[i]
        i += 1
        k += 1

    while j < len(right_list):
        students[k] = right_list[j]
        j += 1
        k += 1


def merge_sort(students, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(students, left, mid)
        merge_sort(students, mid+1, right)
        merge(students, left, mid, right)


# Example usage
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 92)]
merge_sort(students, 0, len(students)-1)
print(students)