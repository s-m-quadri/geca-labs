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
public class PeakInMountainArray {

    // Returns the peak value
    static int findPeakValue(int[] arr) {
        int peakIdx = findPeakIndex(arr);
        return peakIdx == -1 ? Integer.MIN_VALUE : arr[peakIdx];
    }

    // Returns the peak index (or -1 for invalid input)
    static int findPeakIndex(int[] arr) {
        if (arr == null || arr.length == 0) return -1;
        int n = arr.length;
        if (n == 1) return 0;
        // If you want strict mountain assumption (increase then decrease),
        // arrays of length < 3 are handled by simple scan:
        if (n < 3) {
            return arr[0] >= arr[1] ? 0 : 1;
        }

        int low = 0, high = n - 1;
        while (low < high) {
            int mid = low + (high - low) / 2;
            // Compare with next element only (safe because mid < high when low<high)
            if (arr[mid] < arr[mid + 1]) {
                // ascending — peak is to the right
                low = mid + 1;
            } else {
                // descending or at peak — peak is at mid or to the left
                high = mid;
            }
        }
        // low == high is the peak index
        return low;
    }

    // quick tests
    public static void main(String[] args) {
        int[] a1 = {1, 3, 7, 12, 9, 5, 2};
        System.out.println(findPeakValue(a1));   // 12
        System.out.println(findPeakIndex(a1));   // 3

        int[] a2 = {0, 2, 4, 6, 3, 1};
        System.out.println(findPeakValue(a2));   // 6
        System.out.println(findPeakIndex(a2));   // 3

        int[] a3 = {1, 2}; // small array edge case
        System.out.println(findPeakValue(a3));   // 2
        System.out.println(findPeakIndex(a3));   // 1
    }
}
