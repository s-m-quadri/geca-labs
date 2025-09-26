import heapq

def prim_mst_heap(graph, start=0):
    V = len(graph)
    key = [float('inf')] * V
    parent = [-1] * V
    mstSet = [False] * V
    key[start] = 0

    heap = [(0, start)]
    while heap:
        k, u = heapq.heappop(heap)
        if mstSet[u]:
            continue
        mstSet[u] = True
        for v, weight in enumerate(graph[u]):
            if weight > 0 and not mstSet[v] and weight < key[v]:
                key[v] = weight
                parent[v] = u
                heapq.heappush(heap, (key[v], v))

    mst_edges = []
    for v in range(V):
        if parent[v] != -1:
            mst_edges.append((parent[v], v, graph[parent[v]][v]))
    return mst_edges

graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]
mst = prim_mst_heap(graph, start=0)
print("MST edges:", mst)
