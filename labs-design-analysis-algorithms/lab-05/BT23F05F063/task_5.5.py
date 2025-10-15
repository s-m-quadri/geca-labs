def prim_mst(graph, start=0):
    """
    Prim's algorithm to find MST for a graph represented as adjacency matrix.

    Parameters:
    graph : list of lists
        Adjacency matrix of the graph.
    start : int
        Starting vertex.

    Returns:
    list of tuples
        MST edges in the format (parent, vertex, weight)
    """
    V = len(graph)
    key = [float('inf')] * V
    parent = [-1] * V
    mstSet = [False] * V

    key[start] = 0

    for _ in range(V):
        # Pick vertex u with minimum key not in MST
        min_value = float('inf')
        u = -1
        for v in range(V):
            if not mstSet[v] and key[v] < min_value:
                min_value = key[v]
                u = v

        mstSet[u] = True

        # Update neighbors of u
        for v in range(V):
            weight = graph[u][v]
            if weight > 0 and not mstSet[v] and weight < key[v]:
                key[v] = weight
                parent[v] = u

    # Build MST edge list
    mst_edges = [(parent[v], v, graph[parent[v]][v]) for v in range(V) if parent[v] != -1]
    return mst_edges

# Test case
graph = [
    [0, 2, 0, 6],
    [2, 0, 3, 8],
    [0, 3, 0, 0],
    [6, 8, 0, 0]
]
mst_edges = prim_mst(graph, start=0)
print("MST edges:", mst_edges)
