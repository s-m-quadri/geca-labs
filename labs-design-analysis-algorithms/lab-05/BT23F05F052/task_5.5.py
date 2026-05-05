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
def prim_mst(graph, start):
    V = len(graph)
    key = [float('inf')] * V
    parent = [-1] * V
    mstSet = [False] * V
    key[start] = 0
    for _ in range(V - 1):
        u = min_key(key, mstSet)
        mstSet[u] = True
        update_keys(graph, u, key, parent, mstSet)
    res = []
    for v in range(V):
        if parent[v] != -1:
            res.append((parent[v], v, graph[v][parent[v]]))
    return res
