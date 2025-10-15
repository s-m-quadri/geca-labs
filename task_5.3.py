def update_neighbors(graph, u, key, parent, mstSet):
    """
    Update key and parent arrays for neighbors of vertex u.

    Parameters:
    graph : list of lists
        Adjacency matrix representing the graph.
    u : int
        Selected vertex.
    key : list
        Current key values for all vertices.
    parent : list
        Parent vertices in the MST.
    mstSet : list
        Boolean list indicating vertices included in MST.
    """
    V = len(graph)
    for v in range(V):
        weight = graph[u][v]
        if weight > 0 and not mstSet[v] and weight < key[v]:
            key[v] = weight
            parent[v] = u

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

update_neighbors(graph, u, key, parent, mstSet)

print("key:", key)
print("parent:", parent)
