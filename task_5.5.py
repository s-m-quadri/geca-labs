def prim_mst(graph, start=0):
    """
    Build MST using Prim's algorithm.
    
    graph: adjacency matrix
    start: starting vertex
    Returns: list of MST edges as (parent, vertex, weight)
    """
    V = len(graph)
    
    # Initialization
    key = [float('inf')] * V
    parent = [-1] * V
    mstSet = [False] * V
    
    key[start] = 0  # Start from the given vertex

    for _ in range(V):
        # Step 1: Pick min key vertex not in MST
        u = min_key_vertex(key, mstSet)
        mstSet[u] = True
        
        # Step 2: Update neighbors of u
        update_keys(graph, u, key, parent, mstSet)
    
    # Collect MST edges
    mst_edges = []
    for v in range(V):
        if parent[v] != -1:
            mst_edges.append((parent[v], v, graph[parent[v]][v]))
    
    return mst_edges

# Test case
graph = [
    [0, 2, 0, 6],
    [2, 0, 3, 8],
    [0, 3, 0, 0],
    [6, 8, 0, 0]
]
start = 0

mst_edges = prim_mst(graph, start)
print("MST edges:", mst_edges)
