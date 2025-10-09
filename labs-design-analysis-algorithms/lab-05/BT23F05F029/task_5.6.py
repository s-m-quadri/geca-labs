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
    visited = [False] * V
    key = [float('inf')] * V
    parent = [-1] * V
    
    # Min-heap stores (key, vertex)
    heap = [(0, start)]
    key[start] = 0
    
    while heap:
        weight, u = heapq.heappop(heap)
        if visited[u]:
            continue
        visited[u] = True
        
        # Update neighbors
        for v in range(V):
            if graph[u][v] != 0 and not visited[v] and graph[u][v] < key[v]:
                key[v] = graph[u][v]
                parent[v] = u
                heapq.heappush(heap, (key[v], v))
    
    # Collect MST edges
    mst_edges = [(parent[v], v, graph[parent[v]][v]) for v in range(V) if parent[v] != -1]
    return mst_edges


# --- Test Case ---
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]
start = 0

print(prim_mst_heap(graph, start))


