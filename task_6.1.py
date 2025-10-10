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

def create_edge_list(edges):
    """
    Create and return a list of edges.
    Each edge is represented as a tuple (u, v, w) where:
    u, v are vertices and w is the weight.
    """
    return list(edges)

def add_edge(edge_list, u, v, w):
    """
    Add a single edge to the edge list.
    """
    edge_list.append((u, v, w))
    return edge_list

def print_edges(edges):
    """
    Print edges in a formatted way.
    """
    print("Graph Edges:")
    for i, (u, v, w) in enumerate(edges):
        print(f"  Edge {i}: ({u}, {v}) with weight {w}")
    print(f"Total edges: {len(edges)}")

edges1 = [(0, 1, 4), (0, 2, 3), (1, 2, 1)]
edge_list1 = create_edge_list(edges1)
print("Test Case 1:")
print_edges(edge_list1)

print("\nTest Case 2 - Building edge list step by step:")
edge_list2 = []
add_edge(edge_list2, 0, 1, 10)
add_edge(edge_list2, 0, 2, 6)
add_edge(edge_list2, 0, 3, 5)
add_edge(edge_list2, 1, 3, 15)
add_edge(edge_list2, 2, 3, 4)
print_edges(edge_list2)

print("\nTest Case 3 - Larger graph:")
edges3 = [
    (0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8), (1, 4, 5),
    (2, 4, 7), (3, 4, 9)
]
edge_list3 = create_edge_list(edges3)
print_edges(edge_list3)

print("\nVerification:")
print(f"Original edges: {edges1}")
print(f"Stored edges:   {edge_list1}")
print(f"Lists are equal: {edges1 == edge_list1}")
