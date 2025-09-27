"""
background:
Repeating iterations completes the MST construction.

Task:
Implement full Prim's algorithm for a given adjacency matrix.

Instruction:B
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
  
import math
def prim_mst(graph, start=0):
    V = len(graph)
    key = [math.inf] * V
    parent = [-1] * V
    mstSet = [False] * V

    key[start] = 0  # start from given vertex

    for _ in range(V - 1):
        # Step 1: Pick min-key vertex not in MST
        u = min((k, v) for v, k in enumerate(key) if not mstSet[v])[1]
        mstSet[u] = True

        # Step 2: Update neighbors
        for v in range(V):
            if graph[u][v] != 0 and not mstSet[v] and graph[u][v] < key[v]:
                key[v] = graph[u][v]
                parent[v] = u

    # Collect MST edges (skip start vertex since parent[start] = -1)
    mst_edges = [(parent[v], v, graph[parent[v]][v]) for v in range(V) if parent[v] != -1]
    return mst_edges


# --- Test Case ---
graph = [
    [0, 2, 0, 6],
    [2, 0, 3, 8],
    [0, 3, 0, 0],
    [6, 8, 0, 0]
]
start = 0

print(prim_mst(graph, start))
# Expected: [(0,1,2),(1,2,3),(0,3,6)]
 