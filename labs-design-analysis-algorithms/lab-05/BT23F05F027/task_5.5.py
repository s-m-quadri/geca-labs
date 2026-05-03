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
    
    # Initialize key, parent, and mstSet arrays
    key = [float('inf')] * V
    parent = [-1] * V
    mstSet = [False] * V
    
    # Start from the given vertex
    key[start] = 0
    
    for _ in range(V):
        # Step 1: Find the vertex with the minimum key not in mstSet
        min_value = float('inf')
        u = -1
        for v in range(V):
            if not mstSet[v] and key[v] < min_value:
                min_value = key[v]
                u = v
                
        # Include this vertex in mstSet
        mstSet[u] = True
        
        # Step 2: Update key and parent for neighbors of u
        for v in range(V):
            if graph[u][v] > 0 and not mstSet[v] and graph[u][v] < key[v]:
                key[v] = graph[u][v]
                parent[v] = u
                
    # Collecting the MST edges
    mst_edges = []
    for v in range(V):
        if parent[v] != -1:
            mst_edges.append((parent[v], v, graph[parent[v]][v]))
    
    return mst_edges
# Example usage
graph = [
    [0, 2, 0, 6],
    [2, 0, 3, 8],                   
    [0, 3, 0, 0],
    [6, 8, 0, 0]
]
mst = prim_mst(graph, start=0)
print("MST edges (parent, vertex, weight):", mst)       
