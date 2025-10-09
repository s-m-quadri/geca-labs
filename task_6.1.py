# Task 6.1: Representing Graph Edges
# -----------------------------------

def store_edges(edge_list):
    """
    Function to store all graph edges.
    Each edge is a tuple in the form (u, v, w)
    where:
        u = source vertex
        v = destination vertex
        w = weight of the edge
    """
    edges = []  # initialize an empty list to store edges
    
    for edge in edge_list:
        edges.append(edge)
    
    return edges


# Example Test
input_edges = [(0, 1, 4), (0, 2, 3), (1, 2, 1)]
stored_edges = store_edges(input_edges)
print("Stored edges:", stored_edges)
