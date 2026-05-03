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
    """Merge two sorted lists into a single sorted list."""
    result = []
    i = j = 0

    
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1

    result.extend(list1[i:])

   
    result.extend(list2[j:])

    return result

if __name__ == "__main__":
 
    list1 = [1, 3, 5]
    list2 = [2, 4, 6]
    print("List 1:", list1)
    print("List 2:", list2)
    merged = merge_sorted_lists(list1, list2)
    print("Merged:", merged)


    print("\nAdditional test cases:")

    
    list3 = [1, 5, 9, 10, 15, 20]
    list4 = [2, 3, 8, 13]
    print("List 3:", list3)
    print("List 4:", list4)
    merged2 = merge_sorted_lists(list3, list4)
    print("Merged:", merged2)

    
    list5 = []
    list6 = [1, 2, 3]
    print("List 5:", list5)
    print("List 6:", list6)
    merged3 = merge_sorted_lists(list5, list6)
    print("Merged:", merged3)