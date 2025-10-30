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
    """
    Prim's algorithm using a min-heap. Assumes adjacency matrix input (list of lists).
    Returns list of edges as (parent, vertex, weight).
    """
    V = len(graph)
    if V == 0:
        return []

    key = [float("inf")] * V
    parent = [-1] * V
    visited = [False] * V

    key[start] = 0
    heap = [(0, start)]

    edges = []

    while heap:
        k, u = heapq.heappop(heap)
        if visited[u]:
            continue
        visited[u] = True
        # when u is not the start, parent[u] holds the connecting vertex
        if parent[u] != -1:
            edges.append((parent[u], u, k))
        # explore neighbors
        for v, weight in enumerate(graph[u]):
            if weight != 0 and not visited[v] and weight < key[v]:
                key[v] = weight
                parent[v] = u
                heapq.heappush(heap, (weight, v))
    return edges
