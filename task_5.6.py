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

def prims_mst_optimized(graph, start=0):
    V = len(graph)
    
    key = [float('inf')] * V
    parent = [-1] * V
    in_mst = [False] * V
    
    key[start] = 0
    
    min_heap = [(0, start)]
    
    mst_edges = []
    
    while min_heap:
        current_key, u = heapq.heappop(min_heap)
        
        if in_mst[u]:
            continue
        
        in_mst[u] = True
        
        if parent[u] != -1:
            weight = graph[u][parent[u]]
            mst_edges.append((parent[u], u, weight))
        
        for v in range(V):
            if (not in_mst[v] and 
                graph[u][v] != 0 and 
                graph[u][v] < key[v]):
                key[v] = graph[u][v]
                parent[v] = u
                heapq.heappush(min_heap, (float(key[v]), v))
    
    return mst_edges

def adjacency_list_to_matrix(adj_list, V):
    graph = [[0] * V for _ in range(V)]
    for u in range(V):
        for v, weight in adj_list[u]:
            graph[u][v] = weight
            graph[v][u] = weight
    return graph

def prims_mst_adj_list(adj_list, start=0):
    V = len(adj_list)
    
    key = [float('inf')] * V
    parent = [-1] * V
    in_mst = [False] * V
    
    key[start] = 0
    
    min_heap = [(0, start)]
    
    mst_edges = []
    
    while min_heap:
        current_key, u = heapq.heappop(min_heap)
        
        if in_mst[u]:
            continue
        
        in_mst[u] = True
        
        if parent[u] != -1:
            weight = current_key
            mst_edges.append((parent[u], u, weight))
        
        for v, weight in adj_list[u]:
            if not in_mst[v] and weight < key[v]:
                key[v] = weight
                parent[v] = u
                heapq.heappush(min_heap, (weight, v))
    
    return mst_edges

def print_mst_result(graph_type, graph, start, mst_edges):
    print(f"{graph_type} representation:")
    if isinstance(graph[0], list) and isinstance(graph[0][0], int):
        for i, row in enumerate(graph):
            print(f"  {i}: {row}")
    else:
        for i, adj in enumerate(graph):
            print(f"  {i}: {adj}")
    
    print(f"\nStarting vertex: {start}")
    print(f"MST edges: {mst_edges}")
    
    total_weight = sum(weight for _, _, weight in mst_edges)
    print(f"Total MST weight: {total_weight}")
    
    print("\nMST edge details:")
    for parent, vertex, weight in mst_edges:
        print(f"  Edge ({parent}, {vertex}) with weight {weight}")

graph_matrix = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]
start = 0

print("Test case 1 - Adjacency Matrix:")
mst_edges1 = prims_mst_optimized(graph_matrix, start)
print_mst_result("Adjacency Matrix", graph_matrix, start, mst_edges1)

print("\n" + "="*70)

adj_list = [
    [(1, 2), (3, 6)],
    [(0, 2), (2, 3), (3, 8), (4, 5)],
    [(1, 3), (4, 7)],
    [(0, 6), (1, 8), (4, 9)],
    [(1, 5), (2, 7), (3, 9)]
]

print("Test case 2 - Adjacency List:")
mst_edges2 = prims_mst_adj_list(adj_list, start)
print_mst_result("Adjacency List", adj_list, start, mst_edges2)

print("\n" + "="*70)

large_graph = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0]
]

print("Test case 3 - Larger graph (9 vertices):")
mst_edges3 = prims_mst_optimized(large_graph, 0)
print_mst_result("Large Adjacency Matrix", large_graph, 0, mst_edges3)