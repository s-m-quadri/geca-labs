
def update_keys_and_parents(graph, u, key, parent, mstSet):
    V = len(graph)
    for v in range(V):
        # Check if there's an edge from u to v, v is not in MST, and weight is less than current key[v]
        if graph[u][v] != 0 and not mstSet[v] and graph[u][v] < key[v]:
            key[v] = graph[u][v]
            parent[v] = u
