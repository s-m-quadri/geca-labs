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
    # Step 1: pick the vertex with minimum key not in MST
    u = min_key_vertex(key, mstSet)
    
    # Step 2: include it in MST
    mstSet[u] = True
    
    # Step 3: update neighbors
    update_keys(graph, u, key, parent, mstSet)
    
    return key, parent, mstSet
