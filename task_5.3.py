def update_keys(graph, u, key, parent, mstSet):
    V = len(graph)
    for v in range(V):
        if graph[u][v] > 0 and not mstSet[v] and graph[u][v] < key[v]:
            key[v] = graph[u][v]
            parent[v] = u

graph = [
    [0, 2, 0],
    [2, 0, 3],
    [0, 3, 0]
]
u = 0
key = [0, float('inf'), float('inf')]
mstSet = [True, False, False]
parent = [-1, -1, -1]

update_keys(graph, u, key, parent, mstSet)
print(key)
print(parent)

