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
public class MountainPeak {
    public static int peakIndexInMountainArray(int[] arr) {
        int low = 0, high = arr.length - 1;
        while (low < high) {
            int mid = low + (high - low) / 2;
            if (arr[mid] < arr[mid + 1]) {
                low = mid + 1;      // rising slope
            } else {
                high = mid;         // falling slope or peak
            }
        }
        return low; // peak index
    }

    public static void main(String[] args) {
        int[] a = {1, 3, 5, 7, 6, 4, 2};
        int idx = peakIndexInMountainArray(a);
        System.out.println(idx + " " + a[idx]); // 3 7
    }
}
