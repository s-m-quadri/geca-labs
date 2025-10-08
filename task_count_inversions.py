
def count_inversions(arr):
    def merge_sort(nums):
        if len(nums) <= 1:
            return nums, 0

        mid = len(nums) // 2
        left, inv_left = merge_sort(nums[:mid])
        right, inv_right = merge_sort(nums[mid:])
        merged, inv_split = merge(left, right)

        # Total inversions = left + right + split
        return merged, inv_left + inv_right + inv_split

    def merge(left, right):
        i = j = inv_count = 0
        merged = []

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
                # All remaining elements in left are greater than right[j]
                inv_count += len(left) - i

        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, inv_count

    _, total_inversions = merge_sort(arr)
    return total_inversions


# Example test cases
if __name__ == "__main__":
    # Test 1: basic example only
    arr = [2, 4, 1, 3, 5]
    print("Number of inversions:", count_inversions(arr))  

    # Test 2: this one is Already sorted
    arr = [1, 2, 3, 4, 5]
    print("Number of inversions:", count_inversions(arr))  

    # Test 3: what if we do it Reverse sorted?
    arr = [5, 4, 3, 2, 1]
    print("Number of inversions:", count_inversions(arr))  

