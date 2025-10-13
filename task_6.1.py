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

#To - do
#Now Completed

def create_edge_list(edges):
    edge_list = []
    for u, v, w in edges:
        edge_list.append((u, v, w))
    return edge_list

# Example (very important)
edges = [(6, 1, 2), (4, 2, 8), (5, 3, 1)]
result = create_edge_list(edges)
print("Edge List:", result)