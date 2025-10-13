def update_keys_and_parents(graph, u, key, parent, mstSet):
    V = len(graph)
    for v in range(V):
        if graph[u][v] and not mstSet[v] and graph[u][v] < key[v]:
            key[v] = graph[u][v]
            parent[v] = u

# Example usage and test
if __name__ == "__main__":
    graph = [
        [0, 2, 0],
        [2, 0, 3],
        [0, 3, 0]
    ]
    u = 0
    key = [0, float('inf'), float('inf')]
    mstSet = [True, False, False]
    parent = [-1, -1, -1]
    update_keys_and_parents(graph, u, key, parent, mstSet)
    print("key =", key)      # Expected: [0, 2, inf]
    print("parent =", parent)  # Expected: [-1, 0, -1]
