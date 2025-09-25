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

def initialize_prim_arrays(V):
    key = [float('inf')] * V
    parent = [-1] * V
    mstSet = [False] * V
    return key, parent, mstSet
