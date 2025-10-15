def update_keys(graph, u, key, parent, mstSet):
    """
    Update key and parent arrays for neighbors of vertex u.

    graph: adjacency matrix
    u: selected vertex
    key: current key values
    parent: parent array
    mstSet: vertices included in MST
    """
    V = len(graph)
    for v in range(V):
        # Check for edge existence, not in MST, and smaller weight
        if graph[u][v] > 0 and not mstSet[v] and graph[u][v] < key[v]:
            key[v] = graph[u][v]
            parent[v] = u

#tests
# Test case
graph = [
    [0, 2, 0],
    [2, 0, 3],
    [0, 3, 0]
]
u = 0
key = [0, float('inf'), float('inf')]
mstSet = [True, False, False]
parent = [-1, -1, -1]

update_keys(graph, u, key, parent, mstSet)
print("Updated key:", key)
print("Updated parent:", parent)
