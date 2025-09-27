# Task 6.2: Sorting Edges
# ------------------------
# Write a function that sorts edges by their weight.
# Use Python's built-in sorted().

# Example:
# Input: [(0,1,4), (0,2,3), (1,2,1)]
# Expected Output: [(1,2,1), (0,2,3), (0,1,4)]

# Hint: Sort using key = lambda x: x[2]
# Tip: Test with 5-6 edges to check order.
def sort_edges(edges):
    """
    Sorts edges by their weight in ascending order.
    
    Args:
        edges: List of tuples (u, v, w)
    
    Returns:
        List of edges sorted by weight
    """
    return sorted(edges, key=lambda x: x[2])

# Test the function
if __name__ == "__main__":
    edges = [(0,1,4), (0,2,3), (1,2,1), (1,3,5), (2,3,2), (3,4,6)]
    print("Original edges:", edges)
    sorted_edges = sort_edges(edges)
    print("Sorted edges:", sorted_edges)