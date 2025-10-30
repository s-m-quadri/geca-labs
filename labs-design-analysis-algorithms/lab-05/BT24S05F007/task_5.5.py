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
from .task_5.1 import init_prim
from .task_5.2 import min_key_index
from .task_5.3 import update_neighbors

def prim_mst(graph, start=0):
    """
    Full Prim's algorithm using adjacency matrix input.
    Returns list of edges as tuples: (parent, vertex, weight)
    """
    V = len(graph)
    key, parent, mstSet = init_prim(V)
    key[start] = 0
    # Repeat V times to include all vertices
    for _ in range(V):
        u = min_key_index(key, mstSet)
        if u == -1:
            break
        mstSet[u] = True
        update_neighbors(graph, u, key, parent, mstSet)

    edges = []
    for v in range(V):
        if parent[v] != -1:
            # weight from adjacency matrix (parent <-> v)
            w = graph[v][parent[v]]
            edges.append((parent[v], v, w))
    return edges
