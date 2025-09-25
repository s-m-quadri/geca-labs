# Puzzle / Learning focus:
# - Given a sorted array of positive numbers, find the smallest missing positive integer.
# - Use binary search thinking to locate the “gap” without checking every element.
# - Challenge: handle edge cases at the start and end of the array.
#
# Example test cases:
# Input: [1, 2, 3, 5, 6]
# Output: 4
#
# Input: [2, 3, 4, 5]
# Output: 1


public class SmallestMissingPositive {
    
    static int findSmallestMissing(int[] arr) {
        int low = 0, high = arr.length - 1;
        
        // Case: if first element is not 1, then 1 is missing
        if (arr[0] != 1) {
            return 1;
        }
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            
            // Expected value at mid = mid + 1
            if (arr[mid] == mid + 1) {
                // No gap till mid, search right
                low = mid + 1;
            } else {
                // Gap exists, search left
                high = mid - 1;
            }
        }
        
        // When loop ends, 'low' points to first mismatch
        return low + 1;
    }

    // Test
    public static void main(String[] args) {
        int[] arr1 = {1, 2, 3, 5, 6};
        System.out.println(findSmallestMissing(arr1)); // Output: 4

        int[] arr2 = {2, 3, 4, 5};
        System.out.println(findSmallestMissing(arr2)); // Output: 1

        int[] arr3 = {1, 2, 3, 4, 5};
        System.out.println(findSmallestMissing(arr3)); // Output: 6

        int[] arr4 = {1, 3, 4, 5, 6};
        System.out.println(findSmallestMissing(arr4)); // Output: 2
    }
}
