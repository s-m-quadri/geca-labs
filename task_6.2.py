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
    """Sort edges by weight in ascending order."""
    return sorted(edges, key=lambda x: x[2])

# Test the function
if __name__ == "__main__":
    # Test case 1
    edges1 = [(0,1,4), (0,2,3), (1,2,1)]
    sorted_edges1 = sort_edges_by_weight(edges1)
    print("Original edges:", edges1)
    print("Sorted edges:", sorted_edges1)
    
    # Test case 2 - More edges
    edges2 = [(0,1,10), (0,2,6), (0,3,5), (1,3,15), (2,3,4)]
    sorted_edges2 = sort_edges_by_weight(edges2)
    print("\nOriginal edges:", edges2)
    print("Sorted edges:", sorted_edges2)
