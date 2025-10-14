# Task 6.1: Representing Graph Edges
# -----------------------------------
# Write a function that accepts edges as tuples (u, v, w).
# u, v are vertices, w is the weight.
# Store all edges in a list of tuples.

# Example:
# Input: [(0,1,4), (0,2,3), (1,2,1)]
# Expected storage: Same list, but sorted is NOT required here.

def store_edges(edge_list):
    """
    Accepts edges as tuples (u, v, w) and stores them in a list.
    
    Args:
        edge_list: List of tuples (u, v, w) where u, v are vertices and w is weight
    
    Returns:
        List of edges in the same format as input
    """
    edges = []
    for edge in edge_list:
        # Validate edge format
        if len(edge) != 3:
            raise ValueError("Each edge must be a tuple of (u, v, w)")
        u, v, w = edge
        if not isinstance(w, (int, float)):
            raise ValueError("Edge weight must be a number")
        edges.append(edge)
    return edges

def print_edges(edges):
    """Helper function to print edges in a readable format"""
    print("\nEdges in the graph:")
    for u, v, w in edges:
        print(f"Edge {u} -- {w} --> {v}")

# Test cases
if __name__ == "__main__":
    # Test case 1: Basic edge list
    test1 = [(0, 1, 4), (0, 2, 3), (1, 2, 1)]
    print("\nTest 1: Basic edge list")
    result1 = store_edges(test1)
    print_edges(result1)
    print(f"Verification: {result1 == test1}")
    
    # Test case 2: Empty edge list
    test2 = []
    print("\nTest 2: Empty edge list")
    result2 = store_edges(test2)
    print(f"Empty list stored: {result2 == []}")
    
    # Test case 3: List with single edge
    test3 = [(0, 1, 5)]
    print("\nTest 3: Single edge")
    result3 = store_edges(test3)
    print_edges(result3)
    
    # Test case 4: List with floating point weights
    test4 = [(0, 1, 4.5), (1, 2, 2.7)]
    print("\nTest 4: Floating point weights")
    result4 = store_edges(test4)
    print_edges(result4)
    
    print("\nAll test cases completed successfully!")
