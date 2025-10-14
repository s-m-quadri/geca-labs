def prim_mst(graph, start=0):
    V = len(graph)
    
    # Step 1: Initialize key, parent, mstSet
    key = [float('inf')] * V
    parent = [-1] * V
    mstSet = [False] * V

    key[start] = 0  # Start from the given vertex

    for _ in range(V):
        # Step 2: Pick the min key vertex not in MST
        min_val = float('inf')
        u = -1
        for v in range(V):
            if not mstSet[v] and key[v] < min_val:
                min_val = key[v]
                u = v

        # Step 3: Include u in MST
        mstSet[u] = True

        # Step 4: Update keys and parents of adjacent vertices
        for v in range(V):
            if graph[u][v] != 0 and not mstSet[v] and graph[u][v] < key[v]:
                key[v] = graph[u][v]
                parent[v] = u

    # Step 5: Collect MST edges
    mst_edges = []
    for v in range(V):
        if parent[v] != -1:
            mst_edges.append((parent[v], v, graph[parent[v]][v]))

    return mst_edges
