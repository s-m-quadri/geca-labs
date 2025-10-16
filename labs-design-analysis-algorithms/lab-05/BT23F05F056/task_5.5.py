"""
Background:
Repeating iterations completes the MST construction.

Task:
Implement full Prim's algorithm for a given adjacency matrix.

Instruction:
- Input: adjacency matrix graph, start vertex.
- Output: list of MST edges (parent, vertex, weight).

Tip:
Use previous helper functions: min-key selection, key updates.

Test case:
graph = [
 [0, 2, 0, 6],
 [2, 0, 3, 8],
 [0, 3, 0, 0],
 [6, 8, 0, 0]
]
start = 0
# Expected MST edges: [(0,1,2),(1,2,3),(0,3,6)]
"""
<<<<<<< HEAD
def find_min_key_vertex(key, mstSet):
    V = len(key)
    min_key = float('inf')
    min_index = -1
    
    for v in range(V):
        if not mstSet[v] and key[v] < min_key:
            min_key = key[v]
            min_index = v
    
    return min_index

def update_keys(graph, u, key, parent, mstSet):
    V = len(graph)
    
    for v in range(V):
        if (not mstSet[v] and 
            graph[u][v] != 0 and 
            graph[u][v] < key[v]):
            key[v] = graph[u][v]
            parent[v] = u

def prims_mst(graph, start=0):
    V = len(graph)
    
    key = [float('inf')] * V
    parent = [-1] * V
    mstSet = [False] * V
    
    key[start] = 0
    
    mst_edges = []
    
    for _ in range(V):
        u = find_min_key_vertex(key, mstSet)
        
        if u == -1:
            break
        
        mstSet[u] = True
        
        if parent[u] != -1:
            weight = graph[u][parent[u]]
            mst_edges.append((parent[u], u, weight))
        
        update_keys(graph, u, key, parent, mstSet)
    
    return mst_edges

def print_mst_result(graph, start, mst_edges):
    print(f"Graph adjacency matrix:")
    for i, row in enumerate(graph):
        print(f"  {i}: {row}")
    
    print(f"\nStarting vertex: {start}")
    print(f"MST edges: {mst_edges}")
    
    total_weight = sum(weight for _, _, weight in mst_edges)
    print(f"Total MST weight: {total_weight}")
    
    print("\nMST edge details:")
    for parent, vertex, weight in mst_edges:
        print(f"  Edge ({parent}, {vertex}) with weight {weight}")
=======
def prim_mst(graph, start=0):
    V = len(graph)
    key = [float('inf')] * V
    parent = [-1] * V
    mstSet = [False] * V
    key[start] = 0

    for _ in range(V):
        u = -1
        min_val = float('inf')
        for i in range(V):
            if not mstSet[i] and key[i] < min_val:
                min_val = key[i]
                u = i
        mstSet[u] = True

        for v in range(V):
            if graph[u][v] > 0 and not mstSet[v] and graph[u][v] < key[v]:
                key[v] = graph[u][v]
                parent[v] = u

    mst_edges = []
    for v in range(V):
        if parent[v] != -1:
            mst_edges.append((parent[v], v, graph[parent[v]][v]))
    return mst_edges
>>>>>>> fce9ab5 (Added Lab 5)

graph = [
    [0, 2, 0, 6],
    [2, 0, 3, 8],
    [0, 3, 0, 0],
    [6, 8, 0, 0]
]
<<<<<<< HEAD
start = 0

mst_edges = prims_mst(graph, start)
print_mst_result(graph, start, mst_edges)

print("\n" + "="*60)

graph2 = [
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
start2 = 0

print("Test case 2 - Larger graph:")
mst_edges2 = prims_mst(graph2, start2)
print_mst_result(graph2, start2, mst_edges2)
=======
mst = prim_mst(graph, start=0)
print("MST edges:", mst)
>>>>>>> fce9ab5 (Added Lab 5)
