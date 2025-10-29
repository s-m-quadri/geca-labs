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
    Return a new list of edges sorted by weight.
    edges: iterable of (u, v, w)
    """
    return sorted(list(edges), key=lambda e: e[2])

if __name__ == "__main__":
    example = [(0,1,4), (0,2,3), (1,2,1)]
    print("Sorted:", sort_edges(example))
