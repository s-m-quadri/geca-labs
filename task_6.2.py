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
    Sorts a list of edges by their weight using Python's built-in sorted().
    
    Parameters:
    edges (list of tuples): Each tuple is in the form (u, v, w), 
                            where u and v are vertices, and w is the weight.

    Returns:
    list of tuples: Edges sorted in ascending order by weight.
    """
    return sorted(edges, key=lambda x: x[2])

# Example usage:
edges = [(0, 1, 4), (0, 2, 3), (1, 2, 1)]
sorted_edges = sort_edges_by_weight(edges)
print("Sorted edges by weight:", sorted_edges)
