def prim_mst(graph, start=0):
    V = len(graph)
    key = [float('inf')] * V
    parent = [-1] * V
    mstSet = [False] * V
    key[start] = 0

    for _ in range(V):
        u = min_key_vertex(key, mstSet)
        mstSet[u] = True
        update_keys(graph, u, key, parent, mstSet)

    mst_edges = []
    for v in range(V):
        if parent[v] != -1:
            mst_edges.append((parent[v], v, graph[parent[v]][v]))
    return mst_edges

graph = [
    [0, 2, 0, 6],
    [2, 0, 3, 8],
    [0, 3, 0, 0],
    [6, 8, 0, 0]
]
print(prim_mst(graph, start=0))
