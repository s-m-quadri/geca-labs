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
def prim_iteration(graph, key, parent, mstSet):
    """
    Performs one iteration of Prim's algorithm:
    - Selects min-key vertex
    - Updates neighbors
    """
    # Step 1: Pick the vertex with minimum key not yet in MST
    u = min_key_vertex(key, mstSet)

    # Step 2: Include it in MST
    mstSet[u] = True

    # Step 3: Update keys of neighbors
    update_keys(graph, u, key, parent, mstSet)


# -------------------------
# Helper functions from previous steps
# -------------------------
def min_key_vertex(key, mstSet):
    min_val = float('inf')
    min_idx = -1
    for v in range(len(key)):
        if not mstSet[v] and key[v] < min_val:
            min_val = key[v]
            min_idx = v
    return min_idx

def update_keys(graph, u, key, parent, mstSet):
    V = len(graph)
    for v in range(V):
        weight = graph[u][v]
        if weight > 0 and not mstSet[v] and weight < key[v]:
            key[v] = weight
            parent[v] = u


# -------------------------
# Example usage
# -------------------------
graph = [
    [0, 1, 4],
    [1, 0, 2],
    [4, 2, 0]
]
key = [0, float('inf'), float('inf')]
mstSet = [True, False, False]
parent = [-1, -1, -1]

prim_iteration(graph, key, parent, mstSet)

print("key after iteration:", key)      # [0, 1, 2]
print("parent after iteration:", parent) # [-1, 0, 1]
print("mstSet after iteration:", mstSet) # [True, True, False]

