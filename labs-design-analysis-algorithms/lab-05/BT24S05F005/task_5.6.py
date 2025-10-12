"""
import heapq

def prim_mst_heap(graph, start=0):
    V = len(graph)
    key = [float('inf')] * V
    parent = [-1] * V
    in_mst = [False] * V

    # Min-heap to pick minimum weight edge (key, vertex)
    min_heap = [(0, start)]
    key[start] = 0

    while min_heap:
        k, u = heapq.heappop(min_heap)
        if in_mst[u]:
            continue  # Skip if already in MST

        in_mst[u] = True

        # Update neighbors
        for v in range(V):
            weight = graph[u][v]
            if weight != 0 and not in_mst[v] and weight < key[v]:
                key[v] = weight
                parent[v] = u
                heapq.heappush(min_heap, (key[v], v))

    # Construct MST edg
