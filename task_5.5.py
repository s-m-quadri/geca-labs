"""
Background:
Repeating iterations completes the MST construction.

Task:
Implement full Prim's algorithm for a given adjacency matrix.

Instruction:
- Input: adjacency matrix graph, start vertex.
- Output: list of MST edges (parent, vertex, weight).

Tip:
Use previous helper functions: min-key selection, key updates.

Test case:
graph = [
 [0, 2, 0, 6],
 [2, 0, 3, 8],
 [0, 3, 0, 0],
 [6, 8, 0, 0]
]
start = 0
# Expected MST edges: [(0,1,2),(1,2,3),(0,3,6)]
"""

def prim_mst(graph, start=0):
    n = len(graph)
    key = [float('inf')] * n
    parent = [-1] * n
    mstSet = [False] * n
    key[start] = 0

    for _ in range(n):
        u = -1
        min_value = float('inf')
        for v in range(n):
            if not mstSet[v] and key[v] < min_value:
                min_value = key[v]
                u = v
        mstSet[u] = True
        for v in range(n):
            if graph[u][v] != 0 and not mstSet[v] and graph[u][v] < key[v]:
                key[v] = graph[u][v]
                parent[v] = u

    mst_edges = []
    for v in range(n):
        if parent[v] != -1:
            mst_edges.append((parent[v], v, graph[parent[v]][v]))

    return mst_edges

graph = [
    [0, 2, 0, 6],
    [2, 0, 3, 8],
    [0, 3, 0, 0],
    [6, 8, 0, 0]
]
#test case
mst = prim_mst(graph, start=0)
print("MST edges:", mst)
