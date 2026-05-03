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
public class SmallestMissing {
    static int findSmallestMissing(int[] arr) {
        int n = arr.length;

        // Case 1: if first element > 1, missing = 1
        if (arr[0] != 1) return 1;

        int low = 0, high = n - 1;
        while (low <= high) {
            int mid = (low + high) / 2;
            
            if (arr[mid] == mid + 1) {
                low = mid + 1; // no gap yet
            } else {
                high = mid - 1; // gap earlier
            }
        }
        return low + 1; // smallest missing
    }

    public static void main(String[] args) {
        int[] arr1 = {1, 2, 3, 5, 6};
        int[] arr2 = {2, 3, 4};
        int[] arr3 = {1, 2, 3, 4, 5};
        
        System.out.println(findSmallestMissing(arr1)); // 4
        System.out.println(findSmallestMissing(arr2)); // 1
        System.out.println(findSmallestMissing(arr3)); // 6
    }
}
