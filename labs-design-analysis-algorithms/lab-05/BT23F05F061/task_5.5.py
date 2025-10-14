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
    V = len(graph)
    
    # Step 1: Initialize arrays
    key = [float('inf')] * V
    parent = [-1] * V
    mstSet = [False] * V
    
    key[start] = 0  # Start vertex
    
    # Step 2: Repeat V-1 times
    for _ in range(V - 1):
        # Find min key vertex not yet in MST
        min_val = float('inf')
        u = -1
        for v in range(V):
            if not mstSet[v] and key[v] < min_val:
                min_val = key[v]
                u = v
        
        # Add this vertex to MST
        mstSet[u] = True
        
        # Update keys and parents of adjacent vertices
        for v in range(V):
            if graph[u][v] > 0 and not mstSet[v] and graph[u][v] < key[v]:
                key[v] = graph[u][v]
                parent[v] = u
    
    # Step 3: Collect MST edges
    mst_edges = []
    for v in range(V):
        if parent[v] != -1:  # skip start vertex
            mst_edges.append((parent[v], v, graph[v][parent[v]]))
    
    return mst_edges
graph = [
    [0, 2, 0, 6],
    [2, 0, 3, 8],
    [0, 3, 0, 0],
    [6, 8, 0, 0]
]
start = 0

mst = prim_mst(graph, start)
print(mst)
