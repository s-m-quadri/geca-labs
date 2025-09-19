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

def merge_sorted_lists(list1, list2):
    """Merge two sorted lists into a single sorted list."""
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
    result.extend(list1[i:])
    
    # Add remaining elements from list2 (if any)
    result.extend(list2[j:])
    
    return result

if __name__ == "__main__":
    # Test case from the example
    list1 = [1, 3, 5]
    list2 = [2, 4, 6]
    print("List 1:", list1)
    print("List 2:", list2)
    merged = merge_sorted_lists(list1, list2)
    print("Merged:", merged)
    
    # Additional test cases
    print("\nAdditional test cases:")
    
    # Test with different lengths
    list3 = [1, 5, 9, 10, 15, 20]
    list4 = [2, 3, 8, 13]
    print("List 3:", list3)
    print("List 4:", list4)
    merged2 = merge_sorted_lists(list3, list4)
    print("Merged:", merged2)
    
    # Test with one empty list
    list5 = []
    list6 = [1, 2, 3]
    print("List 5:", list5)
    print("List 6:", list6)
    merged3 = merge_sorted_lists(list5, list6)
    print("Merged:", merged3)
