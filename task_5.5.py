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

def min_key_vertex(key, mstSet):
    """Find vertex with minimum key value not yet in MST."""
    min_val = float('inf')
    min_index = -1
    for v in range(len(key)):
        if not mstSet[v] and key[v] < min_val:
            min_val = key[v]
            min_index = v
    return min_index


def prims_mst(graph, start=0):
    """Complete Prim's algorithm for MST construction."""
    V = len(graph)
    key = [float('inf')] * V
    parent = [-1] * V
    mstSet = [False] * V

    key[start] = 0  # Start from the given vertex

    for _ in range(V - 1):
        u = min_key_vertex(key, mstSet)
        mstSet[u] = True

        for v in range(V):
            if graph[u][v] != 0 and not mstSet[v] and graph[u][v] < key[v]:
                key[v] = graph[u][v]
                parent[v] = u

    # Build the list of MST edges
    mst_edges = []
    for i in range(V):
        if parent[i] != -1:
            mst_edges.append((parent[i], i, graph[i][parent[i]]))

    return mst_edges


# ✅ Test case
graph = [
    [0, 2, 0, 6],
    [2, 0, 3, 8],
    [0, 3, 0, 0],
    [6, 8, 0, 0]
]
start = 0

mst = prims_mst(graph, start)
print("MST edges:", mst)
# ✅ Expected Output: [(0,1,2), (1,2,3), (0,3,6)]
