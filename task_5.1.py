"""
Background:
Prim's algorithm finds a Minimum Spanning Tree (MST) in a weighted graph.

Task:
Write a function that initializes key[], parent[], mstSet[] arrays for a graph with V vertices.

Instruction:
- Use Python lists.
- Do not implement the full MST yet.

Tip:
Focus only on initialization. Use ∞ for key values and -1 for parent.

Test case:
V = 4
# Expected:
# key = [∞, ∞, ∞, ∞]
# parent = [-1, -1, -1, -1]
# mstSet = [False, False, False, False]
"""
def initialize_prim(V):
    INF = float('inf')
    key = [INF] * V       # Initialize all keys as infinity
    parent = [-1] * V     # Initialize all parents as -1
    mstSet = [False] * V  # Initialize all vertices as not included in MST
    return key, parent, mstSet

# Test case
V = 4
key, parent, mstSet = initialize_prim(V)
print("key =", key)       # [inf, inf, inf, inf]
print("parent =", parent) # [-1, -1, -1, -1]
print("mstSet =", mstSet) # [False, False, False, False]
