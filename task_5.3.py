def update_adjacent_vertices(graph, u, key, parent, mstSet):
    V = len(graph)
    for v in range(V):
        # If there is an edge from u to v, and v is not yet in MST
        if graph[u][v] != 0 and not mstSet[v]:
            # If the edge weight is smaller than the current key[v]
            if graph[u][v] < key[v]:
                key[v] = graph[u][v]
                parent[v] = u
