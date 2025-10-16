def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] >= right[j]:  # descending order
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort_desc(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort_desc(arr[:mid])
    right = merge_sort_desc(arr[mid:])
    return merge(left, right)

if __name__ == "__main__":
    arr = [12,45,23,37,89,34,2,90,11]
    print("Original:", arr)
    sorted_desc = merge_sort_desc(arr)
    print("Sorted (descending):", sorted_desc)
