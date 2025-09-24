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
def minKey(key, mstSet):
    min_val = float("inf")
    min_index = -1
    for v in range(len(key)):
        if not mstSet[v] and key[v] < min_val:
            min_val = key[v]
            min_index = v
    return min_index

def updateKeys(graph, u, key, parent, mstSet):
    V = len(graph)
    for v in range(V):
        if graph[u][v] and not mstSet[v] and graph[u][v] < key[v]:
            key[v] = graph[u][v]
            parent[v] = u

def primMST(graph, start):
    V = len(graph)
    key = [float("inf")] * V
    parent = [-1] * V
    mstSet = [False] * V
    key[start] = 0
    mstSet[start] = True
    updateKeys(graph, start, key, parent, mstSet)
    for _ in range(V - 2):
        u = minKey(key, mstSet)
        mstSet[u] = True
        updateKeys(graph, u, key, parent, mstSet)
    edges = []
    for v in range(V):
        if parent[v] != -1:
            edges.append((parent[v], v, graph[parent[v]][v]))
    return edges

graph = [
    [0, 2, 0, 6],
    [2, 0, 3, 8],
    [0, 3, 0, 0],
    [6, 8, 0, 0]
]
start = 0
print(primMST(graph, start))
