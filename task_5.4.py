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
from .task_5.2 import min_key_index
from .task_5.3 import update_neighbors

def prim_iteration(graph, key, parent, mstSet):
    """
    Perform one iteration of Prim's algorithm:
    - select the min-key vertex not in mstSet
    - mark it as included
    - update its neighbors' keys and parents
    Returns the selected vertex index (u) or -1 if none found.
    """
    u = min_key_index(key, mstSet)
    if u == -1:
        return -1
    mstSet[u] = True
    update_neighbors(graph, u, key, parent, mstSet)
    return u
