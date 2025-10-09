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
    """
    graph: adjacency matrix
    start: starting vertex
    Returns list of MST edges as (parent, vertex, weight)
    """
    V = len(graph)
    
    # Initialization
    key = [float('inf')] * V
    parent = [-1] * V
    mstSet = [False] * V
    
    key[start] = 0  # start from the given vertex
    
    for _ in range(V):
        # Pick vertex u with minimum key not in MST
        u = min_key_vertex(key, mstSet)
        mstSet[u] = True
        
        # Update neighbors
        update_keys(graph, u, key, parent, mstSet)
    
    # Collect MST edges
    mst_edges = []
    for v in range(V):
        if parent[v] != -1:
            mst_edges.append((parent[v], v, graph[v][parent[v]]))
    
    return mst_edges


# -------------------------
# Helper functions
# -------------------------
def min_key_vertex(key, mstSet):
    min_val = float('inf')
    min_idx = -1
    for v in range(len(key)):
        if not mstSet[v] and key[v] < min_val:
            min_val = key[v]
            min_idx = v
    return min_idx

def update_keys(graph, u, key, parent, mstSet):
    V = len(graph)
    for v in range(V):
        weight = graph[u][v]
        if weight > 0 and not mstSet[v] and weight < key[v]:
            key[v] = weight
            parent[v] = u


# -------------------------
# Example usage
# -------------------------
graph = [
    [0, 2, 0, 6],
    [2, 0, 3, 8],
    [0, 3, 0, 0],
    [6, 8, 0, 0]
]
start = 0

mst_edges = prim_mst(graph, start)
print("MST edges:", mst_edges)
# Expected output: [(0,1,2),(1,2,3),(0,3,6)]

