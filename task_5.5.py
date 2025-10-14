def minKey(key, mstSet):
    min_val = float('inf')
    min_index = -1
    for v in range(len(key)):
        if mstSet[v] == False and key[v] < min_val:
            min_val = key[v]
            min_index = v
    return min_index


def updateKeys(graph, u, key, parent, mstSet):
    for v in range(len(graph)):
        if graph[u][v] != 0 and mstSet[v] == False and graph[u][v] < key[v]:
            key[v] = graph[u][v]
            parent[v] = u


def primMST(graph, start=0):
    n = len(graph)
    key = [float('inf')] * n
    parent = [-1] * n
    mstSet = [False] * n

    key[start] = 0

    for _ in range(n):
        u = minKey(key, mstSet)
        mstSet[u] = True
        updateKeys(graph, u, key, parent, mstSet)

    # Build MST edges
    mst_edges = []
    for v in range(n):
        if parent[v] != -1:
            mst_edges.append((parent[v], v, graph[v][parent[v]]))

    return mst_edges


# Test case
graph = [
    [0, 2, 0, 6],
    [2, 0, 3, 8],
    [0, 3, 0, 0],
    [6, 8, 0, 0]
]
start = 0

edges = primMST(graph, start)
print("MST edges:", edges)