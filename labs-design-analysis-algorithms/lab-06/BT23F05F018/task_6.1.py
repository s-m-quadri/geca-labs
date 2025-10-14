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
#edit 
# Task 6.1: Representing Graph Edges
# -----------------------------------


def store_edges(edges):
    
    edge_list = []
    
     for edge in edges:
        edge_list.append(edge)
    
   
    return edge_list



edges_input = [(0, 1, 4), (0, 2, 3), (1, 2, 1)]
stored_edges = store_edges(edges_input)

print("Stored Edges:", stored_edges)
