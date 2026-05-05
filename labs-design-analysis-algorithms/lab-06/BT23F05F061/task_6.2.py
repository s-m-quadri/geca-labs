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
    # Sort edges based on the third element (weight)
    sorted_edges = sorted(edges, key=lambda x: x[2])
    
    # Print to verify
    print("Edges sorted by weight:", sorted_edges)
    
    return sorted_edges

# Example usage
edges_input = [(0, 1, 4), (0, 2, 3), (1, 2, 1), (2, 3, 5), (3, 4, 2)]
sort_edges_by_weight(edges_input)
