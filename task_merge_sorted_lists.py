# You are given two sorted lists `list1` and `list2`.
# Merge them into a single sorted list (ascending order) and return the result.

# Example:
# Input:
# list1 = [1, 3, 5]
# list2 = [2, 4, 6]
# Output:
# [1, 2, 3, 4, 5, 6]

# INSTRUCTIONS:
# - Do NOT use Python's built-in sorted().
# - Implement your own merge function (similar to merge sort's merge step).
# - No recursion required.

# Write your solution here

def merge_sorted_lists(list1, list2):
    """Merge two sorted lists into one sorted list."""
    result = []
    i = j = 0
    
    # Compare elements from both lists and add the smaller one
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    
    # Add remaining elements from list1 (if any)
    while i < len(list1):
        result.append(list1[i])
        i += 1
    
    # Add remaining elements from list2 (if any)
    while j < len(list2):
        result.append(list2[j])
        j += 1
    
    return result

# Test the function
if __name__ == "__main__":
    # Test case 1
    list1 = [1, 3, 5]
    list2 = [2, 4, 6]
    result1 = merge_sorted_lists(list1, list2)
    print(f"List1: {list1}")
    print(f"List2: {list2}")
    print(f"Merged: {result1}")
    print(f"Expected: [1, 2, 3, 4, 5, 6]")
    print()
    
    # Test case 2: Different lengths
    list3 = [1, 5, 9, 10, 15, 20]
    list4 = [2, 3, 8, 13]
    result2 = merge_sorted_lists(list3, list4)
    print(f"List1: {list3}")
    print(f"List2: {list4}")
    print(f"Merged: {result2}")
    print()
    
    # Test case 3: One empty list
    list5 = [1, 2, 3]
    list6 = []
    result3 = merge_sorted_lists(list5, list6)
    print(f"List1: {list5}")
    print(f"List2: {list6}")
    print(f"Merged: {result3}")
    print()
    
    # Test case 4: With duplicates
    list7 = [1, 3, 3, 5]
    list8 = [2, 3, 4, 6]
    result4 = merge_sorted_lists(list7, list8)
    print(f"List1: {list7}")
    print(f"List2: {list8}")
    print(f"Merged: {result4}")
