import heapq

def prim_mst_heap(graph, start=0):
    """
    Build MST using Prim's algorithm with a min-heap.
    
    graph: adjacency matrix
    start: starting vertex
    Returns: list of MST edges as (parent, vertex, weight)
    """
    V = len(graph)
    key = [float('inf')] * V
    parent = [-1] * V
    mstSet = [False] * V
    
    key[start] = 0
    min_heap = [(0, start)]  # (.key, vertex)
    
    while min_heap:
        k, u = heapq.heappop(min_heap)
        if mstSet[u]:
            continue
        mstSet[u] = True
        
        # Update neighbors
        for v in range(V):
            weight = graph[u][v]
            if weight > 0 and not mstSet[v] and weight < key[v]:
                key[v] = weight
                parent[v] = u
                heapq.heappush(min_heap, (key[v], v))
    
    # Collect MST edges
    mst_edges = []
    for v in range(V):
        if parent[v] != -1:
            mst_edges.append((parent[v], v, graph[parent[v]][v]))
    
    return mst_edges

# Test case
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]
start = 0

mst_edges = prim_mst_heap(graph, start)
print("MST edges:", mst_edges)
