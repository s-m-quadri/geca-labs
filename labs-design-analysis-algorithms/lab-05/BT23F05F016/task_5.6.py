import heapq

def prim_mst_heap(graph, start=0):
    V = len(graph)
    key = [float('inf')] * V
    parent = [-1] * V
    in_mst = [False] * V

    key[start] = 0
    min_heap = [(0, start)]  # (key, vertex)

    while min_heap:
        current_key, u = heapq.heappop(min_heap)

        if in_mst[u]:
            continue

        in_mst[u] = True

        for v in range(V):
            weight = graph[u][v]
            if weight != 0 and not in_mst[v] and weight < key[v]:
                key[v] = weight
                parent[v] = u
                heapq.heappush(min_heap, (key[v], v))

    mst_edges = []
    for v in range(V):
        if parent[v] != -1:
            mst_edges.append((parent[v], v, graph[parent[v]][v]))

    return mst_edges
