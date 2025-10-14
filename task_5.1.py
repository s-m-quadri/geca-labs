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
    key = [float('inf')] * V       # All keys initialized to infinity
    parent = [-1] * V              # No parent initially
    mstSet = [False] * V           # None of the vertices are yet included in MST
    return key, parent, mstSet


# Test Case
V = 4
key, parent, mstSet = initialize_prim(V)

print("key =", key)
print("parent =", parent)
print("mstSet =", mstSet)
