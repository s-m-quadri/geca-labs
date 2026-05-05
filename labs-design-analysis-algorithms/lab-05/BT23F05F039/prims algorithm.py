import sys
 
def prim_mst(graph):
    V = len(graph)
    key = [sys.maxsize] * V
    parent = [-1] * V
    key[0] = 0
    mst_set = [False] * V
 
    for _ in range(V):
        u = min((key[v], v) for v in range(V) if not mst_set[v])[1]
        mst_set[u] = True
 
        for v in range(V):
            if graph[u][v] != 0 and not mst_set[v] and graph[u][v] < key[v]:
                key[v] = graph[u][v]
                parent[v] = u
 
    for i in range(1, V):
        print(f"{parent[i]} - {i} \t{graph[i][parent[i]]}")
 
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]
 
 Output
 0 - 1 2
1 - 2 3
0 - 3 6
1 - 4 5