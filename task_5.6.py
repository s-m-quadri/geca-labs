import heapq

def prim_mst_heap(graph, start=0):
    V = len(graph)
    mstSet = [False] * V
    key = [float('inf')] * V
    parent = [-1] * V

    key[start] = 0
    min_heap = [(0, start)]  # (key, vertex)

    while min_heap:
        k, u = heapq.heappop(min_heap)

        if mstSet[u]:
            continue  # Skip if already included
        mstSet[u] = True

        # Update neighbors
        for v in range(V):
            weight = graph[u][v]
            if weight != 0 and not mstSet[v] and weight < key[v]:
                key[v] = weight
                parent[v] = u
                heapq.heappush(min_heap, (key[v], v))

    # Collect MST edges
    mst_edges = []
    for v in range(V):
        if parent[v] != -1:
            mst_edges.append((parent[v], v, graph[parent[v]][v]))

    return mst_edges
