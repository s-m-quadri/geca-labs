# Puzzle / Learning focus:
# - You are given a “mountain array” (numbers increase then decrease).
# - Your task is to find the peak element using binary search ideas.
# - Think carefully about how to compare neighbors to detect the peak.
#
# Example test cases:
# Input: [1, 3, 7, 12, 9, 5, 2]
# Output: 12
#
# Input: [0, 2, 4, 6, 3, 1]
# Output: 6
def find_peak_element(arr):
    low, high = 0, len(arr) - 1

    while low < high:
        mid = low + (high - low) // 2
        
        # If the element to the right is greater, we are on the ascending slope.
        # The peak must be to the right of mid.
        if arr[mid] < arr[mid + 1]:
            low = mid + 1
        # If the element to the right is smaller or equal, we are on the descending slope
        # or at the peak itself. The peak is at mid or to its left.
        else:
            high = mid
            
    # When the loop ends, low and high will point to the peak element.
    return arr[low]

# Example test cases
arr1 = [1, 3, 7, 12, 9, 5, 2]
print(f"Input: {arr1}")
print(f"Output: {find_peak_element(arr1)}")

print("-" * 20)

arr2 = [0, 2, 4, 6, 3, 1]
print(f"Input: {arr2}")
print(f"Output: {find_peak_element(arr2)}")

print("-" * 20)

arr3 = [10, 20, 15, 2, 23, 90, 67]
# Note: This is not a strict mountain array, but the algorithm finds a local peak.
# The problem as defined usually assumes a single peak.
# Let's use a proper mountain array for this example.
arr3_mountain = [10, 20, 30, 40, 25, 15]
print(f"Input: {arr3_mountain}")
print(f"Output: {find_peak_element(arr3_mountain)}")
