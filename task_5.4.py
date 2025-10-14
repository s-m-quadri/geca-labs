"""
Background:
Prim's algorithm repeats selection and update steps to build MST.

Task:
Combine selection of min-key vertex and neighbor updates in one iteration.

Instruction:
- Implement one iteration of Prim's loop.
- Do not complete entire MST yet.

Tip:
Test on small 3-4 vertex graphs to check updates.

Test case:
graph = [
 [0, 1, 4],
 [1, 0, 2],
 [4, 2, 0]
]
key = [0, ∞, ∞]
mstSet = [True, False, False]
parent = [-1, -1, -1]
# Expected after iteration:
# key = [0, 1, 2]
# parent = [-1, 0, 1]
"""

def min_key_vertex(key, mstSet):
    """Find vertex with minimum key value not yet in MST."""
    min_val = float('inf')
    min_index = -1
    for v in range(len(key)):
        if not mstSet[v] and key[v] < min_val:
            min_val = key[v]
            min_index = v
    return min_index


def update_keys(graph, u, key, parent, mstSet):
    """Update key[] and parent[] for adjacent vertices of u."""
    V = len(graph)
    for v in range(V):
        if graph[u][v] != 0 and not mstSet[v] and graph[u][v] < key[v]:
            key[v] = graph[u][v]
            parent[v] = u


def prims_one_iteration(graph, key, parent, mstSet):
    """Perform one full iteration of Prim’s main loop."""
    u = min_key_vertex(key, mstSet)  # Step 1: pick min key vertex
    mstSet[u] = True                 # Step 2: include it in MST
    update_keys(graph, u, key, parent, mstSet)  # Step 3: update neighbors


# ✅ Test case
graph = [
    [0, 1, 4],
    [1, 0, 2],
    [4, 2, 0]
]
key = [0, float('inf'), float('inf')]
mstSet = [True, False, False]
parent = [-1, -1, -1]

# Perform one iteration
prims_one_iteration(graph, key, parent, mstSet)

print("Updated key:", key)       # Expected: [0, 1, 2]
print("Updated parent:", parent) # Expected: [-1, 0, 1]
