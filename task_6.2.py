# Task 6.2: Sorting Edges
# ------------------------
# Write a function that sorts edges by their weight.
# Use Python's built-in sorted().

# Example:
# Input: [(0,1,4), (0,2,3), (1,2,1)]
# Expected Output: [(1,2,1), (0,2,3), (0,1,4)]

# Hint: Sort using key = lambda x: x[2]
# Tip: Test with 5-6 edges to check order.
def sort_edges_by_weight(edges):
    """
    Sorts a list of edges based on their weight (3rd element in the tuple).

    Parameters:
    edges (list of tuples): Each tuple is (u, v, w), where w is the weight.

    Returns:
    list of tuples: Sorted edges by weight.
    """
    return sorted(edges, key=lambda x: x[2])

# Example usage:
unsorted_edges = [(0, 1, 4), (0, 2, 3), (1, 2, 1), (2, 3, 5), (1, 3, 2)]
sorted_edges = sort_edges_by_weight(unsorted_edges)
print("Sorted edges by weight:", sorted_edges)
#output
Sorted edges by weight: [(1, 2, 1), (1, 3, 2), (0, 2, 3), (0, 1, 4), (2, 3, 5)]
