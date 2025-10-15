def _merge_count(left, right):
    """Merge two sorted lists and count cross inversions (left[i] > right[j])."""
    i = j = 0
    merged = []
    inv_count = 0
    n_left = len(left)

    while i < n_left and j < len(right):
        # if left element <= right element, no new inversion with this left element
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            # left[i] > right[j] => every remaining element in left from i..end
            # forms an inversion with right[j]
            merged.append(right[j])
            inv_count += (n_left - i)
            j += 1

    # append leftovers
    if i < n_left:
        merged.extend(left[i:])
    if j < len(right):
        merged.extend(right[j:])

    return merged, inv_count


def _merge_sort_count(arr):
    """Recursively sort arr and return (sorted_arr, inversion_count)."""
    n = len(arr)
    if n <= 1:
        return arr[:], 0

    mid = n // 2
    left_sorted, left_inv = _merge_sort_count(arr[:mid])
    right_sorted, right_inv = _merge_sort_count(arr[mid:])
    merged, cross_inv = _merge_count(left_sorted, right_sorted)

    return merged, left_inv + right_inv + cross_inv


def count_inversions(arr):
    """
    Count inversions in arr (pairs i < j with arr[i] > arr[j]).
    Returns the inversion count (int).
    """
    _, inv_count = _merge_sort_count(arr)
    return inv_count


# Example / quick test
if __name__ == "__main__":
    example = [2, 4, 1, 3, 5]
    print("Array:", example)
    print("Inversion count:", count_inversions(example))  # expected 3
