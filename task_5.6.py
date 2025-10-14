import heapq

def prim_mst_heap(graph, start=0):
    """
    Prim's algorithm using min-heap for efficient MST construction.

    Parameters:
    graph : list of lists
        Adjacency matrix of the graph
    start : int
        Starting vertex

    Returns:
    list of tuples
        MST edges in the format (parent, vertex, weight)
    """
    V = len(graph)
    key = [float('inf')] * V
    parent = [-1] * V
    in_mst = [False] * V

    key[start] = 0
    min_heap = [(0, start)]  # (key, vertex)

    while min_heap:
        k, u = heapq.heappop(min_heap)
        if in_mst[u]:
            continue
        in_mst[u] = True

        # Update neighbors
        for v in range(V):
            weight = graph[u][v]
            if weight > 0 and not in_mst[v] and weight < key[v]:
                key[v] = weight
                parent[v] = u
                heapq.heappush(min_heap, (key[v], v))

    # Build MST edge list
    mst_edges = [(parent[v], v, graph[parent[v]][v]) for v in range(V) if parent[v] != -1]
    return mst_edges

# Test case
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]
mst_edges = prim_mst_heap(graph, start=0)
print("MST edges:", mst_edges)
