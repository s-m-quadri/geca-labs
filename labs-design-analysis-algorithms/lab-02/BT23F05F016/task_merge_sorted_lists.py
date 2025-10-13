# You are given two sorted lists `list1` and `list2`.
# Merge them into a single sorted list (ascending order) and return the result.

# Example:
# Input:
# list1 = [1, 3, 5]
# list2 = [2, 4, 6]
# Output:
# [1, 2, 3, 4, 5, 6]

# INSTRUCTIONS:
# - Do NOT use Python's built-in sorted().
# - Implement your own merge function (similar to merge sort's merge step).
# - No recursion required.

# Write your solution here
import java.util.*;

public class MergeSortedLists {
    public static List<Integer> mergeLists(int[] list1, int[] list2) {
        List<Integer> merged = new ArrayList<>();
        int i = 0, j = 0;

        while (i < list1.length && j < list2.length) {
            if (list1[i] <= list2[j]) {
                merged.add(list1[i++]);
            } else {
                merged.add(list2[j++]);
            }
        }

        while (i < list1.length) merged.add(list1[i++]);
        while (j < list2.length) merged.add(list2[j++]);

        return merged;
    }

    public static void main(String[] args) {
        int[] list1 = {1, 3, 5, 7};
        int[] list2 = {2, 4, 6, 8};

        List<Integer> result = mergeLists(list1, list2);
        System.out.println("Merged List: " + result);
    }
}
