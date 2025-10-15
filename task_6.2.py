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
    Sorts a list of graph edges by their weight.

    Parameters:
    edges (list of tuples): Each tuple is (u, v, w), representing an edge.

    Returns:
    list: Edges sorted in ascending order by weight.
    """
    sorted_edges = sorted(edges, key=lambda x: x[2])
    print("Sorted Edges:", sorted_edges)  # Optional: for verification
    return sorted_edges

# Example usage:
edges = [(0, 1, 4), (0, 2, 3), (1, 2, 1), (2, 3, 5), (1, 3, 2)]
sorted_edges = sort_edges_by_weight(edges)

