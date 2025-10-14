def prim_iteration(graph, key, parent, mstSet):
    """
    Perform one iteration of Prim's algorithm:
    - Pick min key vertex not in MST
    - Update keys and parents of its neighbors
    """
    # Step 1: Pick vertex u with minimum key not in MST
    u = min_key_vertex(key, mstSet)
    mstSet[u] = True  # Include u in MST

    # Stesp 2: Update neighbors of u
    update_keys(graph, u, key, parent, mstSet)
 
# Test case
graph = [
    [0, 1, 4],
    [1, 0, 2],
    [4, 2, 0]
]
key = [0, float('inf'), float('inf')]
mstSet = [True, False, False]
parent = [-1, -1, -1]

# Perform one iteration
prim_iteration(graph, key, parent, mstSet)

print("Key after iteration:", key)
print("Parent after iteration:", parent)
print("MST set:", mstSet)
