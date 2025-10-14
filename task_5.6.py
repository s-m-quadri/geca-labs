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


def prim_mst_optimized(graph, start=0):
    """
    Implement Prim's algorithm using a min-heap for efficiency.
    
    Args:
        graph: Adjacency matrix representation of the graph
        start: Starting vertex (default is 0)
    
    Returns:
        list: List of MST edges as tuples (parent, vertex, weight)
    """
    V = len(graph)
    
    # Track which vertices are in MST
    in_mst = [False] * V
    
    # Store parent and key values
    parent = [-1] * V
    key = [float('inf')] * V
    
    # Min-heap: (key_value, vertex)
    min_heap = []
    
    # Start from the given vertex
    key[start] = 0
    heapq.heappush(min_heap, (0, start))
    
    mst_edges = []
    
    while min_heap:
        # Extract vertex with minimum key
        current_key, u = heapq.heappop(min_heap)
        
        # Skip if vertex is already in MST
        if in_mst[u]:
            continue
        
        # Add vertex to MST
        in_mst[u] = True
        
        # Add edge to MST (skip the starting vertex)
        if parent[u] != -1:
            mst_edges.append((parent[u], u, graph[parent[u]][u]))
        
        # Update keys for adjacent vertices
        for v in range(V):
            # If there's an edge and v is not in MST
            if graph[u][v] != 0 and not in_mst[v]:
                # If we found a better edge
                if graph[u][v] < key[v]:
                    key[v] = graph[u][v]
                    parent[v] = u
                    heapq.heappush(min_heap, (key[v], v))
    
    return mst_edges


# Test case
if __name__ == "__main__":
    graph = [
        [0, 2, 0, 6, 0],
        [2, 0, 3, 8, 5],
        [0, 3, 0, 0, 7],
        [6, 8, 0, 0, 9],
        [0, 5, 7, 9, 0]
    ]
    start = 0
    
    mst_edges = prim_mst_optimized(graph, start)
    
    print("MST edges (parent, vertex, weight):")
    for edge in mst_edges:
        print(f"  {edge}")
    
    print("\nExpected: [(0,1,2), (1,2,3), (1,4,5), (0,3,6)]")
    
    total_weight = sum(edge[2] for edge in mst_edges)
    print(f"\nTotal MST weight: {total_weight}")
    print(f"Expected total weight: 16")
    
    print(f"\nNumber of edges: {len(mst_edges)}")
    print(f"Expected number of edges: 4")
    
    print(f"\nTest passed: {total_weight == 16 and len(mst_edges) == 4}")
