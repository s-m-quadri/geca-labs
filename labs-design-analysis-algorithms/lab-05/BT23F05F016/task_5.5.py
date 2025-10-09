def prim_mst(graph, start):
    V = len(graph)
    key = [float('inf')] * V
    parent = [-1] * V
    mstSet = [False] * V

    key[start] = 0

    for _ in range(V):
        min_key = float('inf')
        u = -1
        for v in range(V):
            if not mstSet[v] and key[v] < min_key:
                min_key = key[v]
                u = v

        if u == -1:
            break  # Disconnected graph

        mstSet[u] = True

        for v in range(V):
            if graph[u][v] != 0 and not mstSet[v] and graph[u][v] < key[v]:
                key[v] = graph[u][v]
                parent[v] = u

    for v in range(V):
        if parent[v] != -1:
            mst_edges.append((parent[v], v, graph[parent[v]][v]))

    return mst_edges
#bhf
