def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i].lower() <= right[j].lower():  # case-insensitive compare
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort_strings(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort_strings(arr[:mid])
    right = merge_sort_strings(arr[mid:])
    return merge(left, right)

if __name__ == "__main__":
    names = ["Charlie", "alice", "Bob", "david"]
    print("Original:", names)
    sorted_names = merge_sort_strings(names)
    print("Sorted (case-insensitive):", sorted_names)
