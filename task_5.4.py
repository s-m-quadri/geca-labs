def prim_one_iteration(graph, key, parent, mstSet):
    # Step 1: Find vertex with minimum key not in MST
    min_val = float('inf')
    u = -1
    for v in range(len(key)):
        if not mstSet[v] and key[v] < min_val:
            min_val = key[v]
            u = v

    # Step 2: Include this vertex in MST set
    mstSet[u] = True

    # Step 3: Update keys and parents of adjacent vertices
    V = len(graph)
    for v in range(V):
        if graph[u][v] != 0 and not mstSet[v] and graph[u][v] < key[v]:
            key[v] = graph[u][v]
            parent[v] = u

