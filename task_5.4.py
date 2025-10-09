def prim_iteration(graph, key, parent, mstSet):
    min_key = float('inf')
    u = -1
    for v in range(len(key)):
        if not mstSet[v] and key[v] < min_key:
            min_key = key[v]
            u = v

    if u == -1:
        return  # All vertices are included or no reachable vertex

    
    mstSet[u] = True

    
    for v in range(len(graph)):
        if graph[u][v] != 0 and not mstSet[v] and graph[u][v] < key[v]:
            key[v] = graph[u][v]
            parent[v] = u

