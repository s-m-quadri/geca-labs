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
    
    # Initialize key, parent, and mstSet arrays
    key = [float('inf')] * V
    parent = [-1] * V
    mstSet = [False] * V
    
    # Min-heap to store (key, vertex)
    min_heap = []
    
    # Start from the given vertex
    key[start] = 0
    heapq.heappush(min_heap, (0, start))
    
    while min_heap:
        # Step 1: Extract the vertex with the minimum key
        min_key, u = heapq.heappop(min_heap)
        
        if mstSet[u]:
            continue
        
        # Include this vertex in mstSet
        mstSet[u] = True
        
        # Step 2: Update key and parent for neighbors of u
        for v in range(V):
            if graph[u][v] > 0 and not mstSet[v] and graph[u][v] < key[v]:
                key[v] = graph[u][v]
                parent[v] = u
                heapq.heappush(min_heap, (key[v], v))
                
    # Collecting the MST edges
    mst_edges = []
    for v in range(V):
        if parent[v] != -1:
            mst_edges.append((parent[v], v, graph[parent[v]][v]))
    
    return mst_edges    
# Example usage
graph = [
    [0, 2, 0, 6, 0],        
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]
mst = prim_mst_heap(graph, start=0)
print("MST edges (parent, vertex, weight):", mst)       
# Expected output: MST edges (parent, vertex, weight): [(0, 1, 2), (1, 2, 3), (1, 4, 5), (0, 3, 6)]