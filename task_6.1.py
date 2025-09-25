# Task 6.1: Representing Graph Edges
# -----------------------------------
# Write a function that accepts edges as tuples (u, v, w).
# u, v are vertices, w is the weight.
# Store all edges in a list of tuples.

# Example:
# Input: [(0,1,4), (0,2,3), (1,2,1)]
# Expected storage: Same list, but sorted is NOT required here.

# Hint: Just create and return the list.
# Tip: Print the list to verify edges.

def store_edges(edges):
    """Store graph edges as list of tuples."""
    return list(edges)

def create_edge_list(*edges):
    """Create edge list from individual edge tuples."""
    return list(edges)

# Test the function
if __name__ == "__main__":
    # Test case 1
    edges1 = [(0,1,4), (0,2,3), (1,2,1)]
    stored_edges = store_edges(edges1)
    print("Edges:", stored_edges)
    
    # Test case 2 - Creating edges directly
    edges2 = create_edge_list((0,1,4), (0,2,3), (1,2,1), (2,3,2))
    print("Created edges:", edges2)