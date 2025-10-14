# Task 6.2: Sorting Edges
# ------------------------
# Write a function that sorts edges by their weight.
# Use Python's built-in sorted().

# Example:
# Input: [(0,1,4), (0,2,3), (1,2,1)]
# Expected Output: [(1,2,1), (0,2,3), (0,1,4)]

# Hint: Sort using key = lambda x: x[2]
# Tip: Test with 5-6 edges to check order.
# sort_edges.py
# Task 6.2: Sorting Edges

def sort_edges_by_weight(edges):
    """
    Sort edges by their weight in ascending order.
    
    Parameters:
    - edges: list of tuples (u, v, w)
    
    Returns:
    - List of edges sorted by weight
    """
    return sorted(edges, key=lambda x: x[2])


# Example usage
edges_input = [(0, 1, 4), (0, 2, 3), (1, 2, 1), (2, 3, 5), (3, 0, 2)]
sorted_edges = sort_edges_by_weight(edges_input)
print("Edges sorted by weight:")
for u, v, w in sorted_edges:
    print(f"Edge from {u} to {v} with weight {w}")
