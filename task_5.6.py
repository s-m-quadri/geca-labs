"""
Background:
Prim's algorithm can be optimized using priority queues.

Task:
Implement MST construction using a min-heap (heapq) to pick min-key vertex efficiently.

Instruction:
- Input: adjacency matrix or adjacency list.
- Output: MST edges with weights.
- Do not use linear search for min-key.

Tip:
Use heapq to maintain (key, vertex). Update keys carefully when a better edge is found.

Test case:
graph = [
 [0, 2, 0, 6, 0],
 [2, 0, 3, 8, 5],
 [0, 3, 0, 0, 7],
 [6, 8, 0, 0, 9],
 [0, 5, 7, 9, 0]
]
start = 0
# Expected MST edges: [(0,1,2),(1,2,3),(1,4,5),(0,3,6)]
"""

import heapq

def prim_mst_heap(graph, start=0):
    V = len(graph)
    
    # Initialize
    key = [float('inf')] * V
    parent = [-1] * V
    inMST = [False] * V
    
    # Start with the given vertex
    key[start] = 0
    
    # Min heap: (key_value, vertex)
    heap = [(0, start)]
    
    mst_edges = []
    
    while heap:
        curr_key, u = heapq.heappop(heap)
        
        # Skip if already processed
        if inMST[u]:
            continue
        
        # Add vertex to MST
        inMST[u] = True
        
        # Add edge to MST (except for starting vertex)
        if parent[u] != -1:
            mst_edges.append((parent[u], u, curr_key))
        
        # Update keys of adjacent vertices
        for v in range(V):
            if (not inMST[v] and 
                graph[u][v] > 0 and 
                graph[u][v] < key[v]):
                key[v] = graph[u][v]
                parent[v] = u
                heapq.heappush(heap, (key[v], v))
    
    return mst_edges
