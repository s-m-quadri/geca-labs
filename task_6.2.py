# Task 6.2: Sorting Edges
# ------------------------
# Write a function that sorts edges by their weight.
# Use Python's built-in sorted().

# Example:
# Input: [(0,1,4), (0,2,3), (1,2,1)]
# Expected Output: [(1,2,1), (0,2,3), (0,1,4)]

# Hint: Sort using key = lambda x: x[2]
# Tip: Test with 5-6 edges to check order.

# Task 6.2: Sorting Edges
# ------------------------

def sort_edges_by_weight(edges):
    sorted_edges = sorted(edges, key=lambda x: x[2])
    return sorted_edges

if __name__ == "__main__":
    edges = [(0, 1, 4), (0, 2, 3), (1, 2, 1), (2, 3, 2), (1, 3, 5)]
    sorted_edges = sort_edges_by_weight(edges)
    print("Original edges:", edges)
    print("Edges sorted by weight:", sorted_edges)
