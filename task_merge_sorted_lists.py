def merge_sorted_lists(list1, list2):
    i, j = 0, 0
    merged = []

    # Merge elements in ascending order
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1

    # Append remaining elements from either list
    merged.extend(list1[i:])
    merged.extend(list2[j:])

    return merged


# Example test cases
if __name__ == "__main__":
    # Test 1
    list1 = [1, 3, 5]
    list2 = [2, 4, 6]
    print("Merged list:", merge_sorted_lists(list1, list2))  # [1, 2, 3, 4, 5, 6]

    # Test 2
    list1 = []
    list2 = [2, 4, 6]
    print("Merged list:", merge_sorted_lists(list1, list2))  # [2, 4, 6]

    # Test 3
    list1 = [1, 5, 9, 10]
    list2 = [2, 3]
    print("Merged list:", merge_sorted_lists(list1, list2))  # [1, 2, 3, 5, 9, 10]
