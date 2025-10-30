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

def _merge_students(left, right):right):
    result = []    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        name_l, score_l = left[i]
        name_r, score_r = right[j]
        # Primary: score descending
        if score_l > score_r:
            result.append(left[i])
            i += 1
        elif score_l < score_r:






























    print(sort_student_scores(students))    students = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 92)]    # Example usageif __name__ == "__main__":    return _merge_sort_students(list(students))    """Return a new list sorted by score desc, then name asc."""def sort_student_scores(students):    return _merge_students(left, right)    right = _merge_sort_students(arr[mid:])    left = _merge_sort_students(arr[:mid])    mid = len(arr) // 2        return arr    if len(arr) <= 1:def _merge_sort_students(arr):    return result    result.extend(right[j:])    result.extend(left[i:])                j += 1                result.append(right[j])            else:                i += 1                result.append(left[i])            if name_l <= name_r:            # Secondary: name ascending        else:            j += 1            result.append(right[j])



























    print(sorted_students)
    sorted_students = sort_student_scores(students)
    students = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 92)]
    # Example usage
if __name__ == "__main__":    return _merge_sort_students(list(students))    """Return a new list sorted by score desc, then name asc."""def sort_student_scores(students):    return _merge_students(left, right)    right = _merge_sort_students(arr[mid:])    left = _merge_sort_students(arr[:mid])    mid = len(arr) // 2        return arr    if len(arr) <= 1:def _merge_sort_students(arr):    return result    result.extend(right[j:])    result.extend(left[i:])                j += 1                result.append(right[j])            else:                i += 1                result.append(left[i])            if name_l <= name_r:            # Secondary: name ascending        else:            j += 1            result.append(right[j])        elif score_l < score_r:            i += 1            result.append(left[i])        if score_l > score_r:        # Primary: score descending        name_r, score_r = right[j]        name_l, score_l = left[i]    while i < len(left) and j < len(right):    i = j = 0    i = j = 0
    while i < len(left) and j < len(right):
        name_l, score_l = left[i]
        name_r, score_r = right[j]
        # Primary: score descending
        if score_l > score_r:
            result.append(left[i])
            i += 1
        elif score_l < score_r:
            result.append(right[j])
            j += 1
        else:
            # Secondary: name ascending
            if name_l <= name_r:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def _merge_sort_students(arr):


    print(sorted_students)
    sorted_students = sort_student_scores(students)
    students = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 92)]
    # Example usage
if __name__ == "__main__":

    return _merge_sort_students(list(students))
    """Return a new list sorted by score desc, then name asc."""
def sort_student_scores(students):

    return _merge_students(left, right)
    right = _merge_sort_students(arr[mid:])
    left = _merge_sort_students(arr[:mid])
    mid = len(arr) // 2
        return arr    if len(arr) <= 1: