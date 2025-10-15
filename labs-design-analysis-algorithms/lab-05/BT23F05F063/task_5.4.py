def prim_one_iteration(graph, key, parent, mstSet):
    """
    Perform one iteration of Prim's algorithm:
    - Select the vertex with minimum key not in MST
    - Update keys and parents for its neighbors
    """
    V = len(graph)
    
    # Step 1: Pick vertex u with minimum key not in MST
    min_value = float('inf')
    u = -1
    for v in range(V):
        if not mstSet[v] and key[v] < min_value:
            min_value = key[v]
            u = v
    
    mstSet[u] = True  # Include u in MST

    # Step 2: Update key and parent for neighbors of u
    for v in range(V):
        weight = graph[u][v]
        if weight > 0 and not mstSet[v] and weight < key[v]:
            key[v] = weight
            parent[v] = u

    return key, parent, mstSet

# Test case
graph = [
    [0, 1, 4],
    [1, 0, 2],
    [4, 2, 0]
]
key = [0, float('inf'), float('inf')]
mstSet = [True, False, False]
parent = [-1, -1, -1]

key, parent, mstSet = prim_one_iteration(graph, key, parent, mstSet)

print("key:", key)
print("parent:", parent)
print("mstSet:", mstSet)
