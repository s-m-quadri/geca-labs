# Given an array of integers, count the number of inversions in the array.
# An inversion is a pair (i, j) such that i < j and arr[i] > arr[j].

# Example:
# Input: [2, 4, 1, 3, 5]
# Output: 3
# Explanation: The inversions are (2,1), (4,1), (4,3)

# INSTRUCTIONS:
# - Implement a function using Merge Sort modification to count inversions efficiently.
# - Target time complexity: O(n log n)
# - Do not use brute force O(n^2) method.

# Write your solution here

   
public class CountInversions {

    // Main function to count inversions
    public static int countInversions(int[] arr) {
        return mergeSortAndCount(arr, 0, arr.length - 1);
    }

    // Recursive Merge Sort that returns inversion count
    private static int mergeSortAndCount(int[] arr, int left, int right) {
        int count = 0;

        if (left < right) {
            int mid = (left + right) / 2;

            // Count inversions in left half
            count += mergeSortAndCount(arr, left, mid);

            // Count inversions in right half
            count += mergeSortAndCount(arr, mid + 1, right);

            // Count inversions during merge
            count += mergeAndCount(arr, left, mid, right);
        }
        return count;
    }

    // Merge two sorted halves and count inversions
    private static int mergeAndCount(int[] arr, int left, int mid, int right) {
        int[] leftArr = new int[mid - left + 1];
        int[] rightArr = new int[right - mid];

        // Copy data
        for (int i = 0; i < leftArr.length; i++)
            leftArr[i] = arr[left + i];
        for (int j = 0; j < rightArr.length; j++)
            rightArr[j] = arr[mid + 1 + j];

        int i = 0, j = 0, k = left, swaps = 0;

        // Merge process
        while (i < leftArr.length && j < rightArr.length) {
            if (leftArr[i] <= rightArr[j]) {
                arr[k++] = leftArr[i++];
            } else {
                arr[k++] = rightArr[j++];
                swaps += (leftArr.length - i); // all remaining elements in leftArr are inversions
            }
        }

        // Copy remaining elements
        while (i < leftArr.length) {
            arr[k++] = leftArr[i++];
        }
        while (j < rightArr.length) {
            arr[k++] = rightArr[j++];
        }

        return swaps;
    }

    // Driver code
    public static void main(String[] args) {
        int[] arr = {2, 4, 1, 3, 5};
        System.out.println("Number of inversions: " + countInversions(arr));
    }
}

     
      
