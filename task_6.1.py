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

def store_graph_edges(edges):
    edge_list = []
    for u, v, w in edges:
        edge_list.append((u, v, w))
    return edge_list

n = int(input("Enter number of edges: "))
edges = []
for i in range(n):
    u = int(input(f"Enter starting vertex of edge {i+1}: "))
    v = int(input(f"Enter ending vertex of edge {i+1}: "))
    w = int(input(f"Enter weight of edge {i+1}: "))
    edges.append((u, v, w))

edge_list = store_graph_edges(edges)
print("Stored edges:", edge_list)
