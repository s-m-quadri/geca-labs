"""
Bdef min_key_vertex(key, mstSet):
    min_val = float('inf')
    min_index = -1
    for v in range(len(key)):
        if not mstSet[v] and key[v] < min_val:
            min_val = key[v]
            min_index = v
    return min_index

def update_keys(graph, u, key, parent, mstSet):
    V = len(graph)
    for v in range(V):
        if graph[u][v] != 0 and not mstSet[v] and graph[u][v] < key[v]:
            key[v] = graph[u][v]
            parent[v] = u

def prim_mst(graph, start):
    V = len(graph)
    key = [float('inf')] * V
    parent = [-1] * V
    mstSet = [False] * V

    key[start] = 0

    for _ in range(V):
        u = min_key_vertex(key, mstSet)
        if u == -1:
            break  # Disconnected component
        mstSet[u] = True
        update_keys(graph, u, key, parent, mstSet)

    # Construct MST edges: (parent[v], v, weight)
    mst_edges = []
    for v in range(V):
        if parent[v] != -1:
            mst_edges.append((parent[v], v, graph[parent[v]][v]))
    return mst_edges
