# Puzzle / Learning focus:
# - You have a sorted array with repeated elements.
# - Count how many times a target number appears using binary search logic.
# - Consider how to find the first and last occurrence efficiently.
#
# Example test cases:
# Input: arr = [1, 2, 2, 2, 3, 4], target = 2
# Output: 3
#
# Input: arr = [5, 5, 5, 5, 5], target = 5
# Output: 5


public class CountOccurrences {
    
    // Function to find the first occurrence
    static int firstOccurrence(int[] arr, int target) {
        int low = 0, high = arr.length - 1, result = -1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            
            if (arr[mid] == target) {
                result = mid;   // store answer
                high = mid - 1; // move left for first occurrence
            } else if (arr[mid] < target) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return result;
    }
    
    // Function to find the last occurrence
    static int lastOccurrence(int[] arr, int target) {
        int low = 0, high = arr.length - 1, result = -1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            
            if (arr[mid] == target) {
                result = mid;   // store answer
                low = mid + 1;  // move right for last occurrence
            } else if (arr[mid] < target) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return result;
    }
    
    // Function to count occurrences
    static int countOccurrences(int[] arr, int target) {
        int first = firstOccurrence(arr, target);
        if (first == -1) return 0; // target not found
        int last = lastOccurrence(arr, target);
        return last - first + 1;
    }
    
    // Test
    public static void main(String[] args) {
        int[] arr1 = {1, 2, 2, 2, 3, 4};
        System.out.println(countOccurrences(arr1, 2)); // Output: 3
        
        int[] arr2 = {5, 5, 5, 5, 5};
        System.out.println(countOccurrences(arr2, 5)); // Output: 5
        
        int[] arr3 = {1, 2, 3, 4, 5};
        System.out.println(countOccurrences(arr3, 6)); // Output: 0
    }
}
