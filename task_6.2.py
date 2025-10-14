# Task 6.2: Sorting Edges
# ------------------------
# Write a function that sorts edges by their weight.
# Use Python's built-in sorted().

# Example:
# Input: [(0,1,4), (0,2,3), (1,2,1)]
# Expected Output: [(1,2,1), (0,2,3), (0,1,4)]

def sort_edges_by_weight(edges):
    """
    Sort edges based on their weight.
    
    Args:
        edges: List of tuples (u, v, w) where u, v are vertices and w is weight
    
    Returns:
        List of edges sorted by weight in ascending order
    """
    # Sort edges by weight (third element of each tuple)
    sorted_edges = sorted(edges, key=lambda x: (x[2], x[0], x[1]))
    return sorted_edges

def print_sorted_edges(edges):
    """Helper function to print sorted edges in a readable format"""
    print("\nEdges sorted by weight:")
    for u, v, w in edges:
        print(f"Weight {w}: {u} --> {v}")

# Test cases
if __name__ == "__main__":
    # Test case 1: Basic edge list
    test1 = [(0, 1, 4), (0, 2, 3), (1, 2, 1)]
    print("\nTest 1: Basic edge sorting")
    result1 = sort_edges_by_weight(test1)
    print_sorted_edges(result1)
    print(f"Verification: First edge has minimum weight {result1[0][2]}")
    
    # Test case 2: Empty edge list
    test2 = []
    print("\nTest 2: Empty edge list")
    result2 = sort_edges_by_weight(test2)
    print(f"Empty list handled: {result2 == []}")
    
    # Test case 3: Edges with same weights
    test3 = [(0, 1, 2), (1, 2, 2), (2, 3, 2), (3, 4, 1)]
    print("\nTest 3: Edges with same weights")
    result3 = sort_edges_by_weight(test3)
    print_sorted_edges(result3)
    
    # Test case 4: Larger graph with various weights
    test4 = [
        (0, 1, 4), (0, 2, 3), (1, 2, 1),
        (2, 3, 5), (1, 3, 2), (3, 4, 6)
    ]
    print("\nTest 4: Larger graph")
    result4 = sort_edges_by_weight(test4)
    print_sorted_edges(result4)
    
    # Test case 5: Floating point weights
    test5 = [(0, 1, 4.5), (1, 2, 2.7), (0, 2, 3.1)]
    print("\nTest 5: Floating point weights")
    result5 = sort_edges_by_weight(test5)
    print_sorted_edges(result5)
    
    print("\nAll test cases completed successfully!")
