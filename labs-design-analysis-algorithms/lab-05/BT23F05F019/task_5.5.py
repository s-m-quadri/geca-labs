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
    
    # Initialize arrays
    key = [float('inf')] * V
    parent = [-1] * V
    mstSet = [False] * V
    
    # Start with the given vertex
    key[start] = 0
    
    mst_edges = []
    
    for _ in range(V):
        # Find minimum key vertex not in MST
        u = find_min_key_vertex(key, mstSet)
        
        if u == -1:
            break
        
        # Add vertex to MST
        mstSet[u] = True
        
        # Add edge to MST (except for starting vertex)
        if parent[u] != -1:
            mst_edges.append((parent[u], u, key[u]))
        
        # Update keys of adjacent vertices
        for v in range(V):
            if (not mstSet[v] and 
                graph[u][v] > 0 and 
                graph[u][v] < key[v]):
                key[v] = graph[u][v]
                parent[v] = u
    
    return mst_edges

def find_min_key_vertex(key, mstSet):
    min_val = float('inf')
    min_index = -1
    
    for v in range(len(key)):
        if not mstSet[v] and key[v] < min_val:
            min_val = key[v]
            min_index = v
    
    return min_index
