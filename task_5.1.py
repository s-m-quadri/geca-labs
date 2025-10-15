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
    # Initialize key[], parent[], and mstSet[] arrays
    key = [float('inf')] * V      # ∞ for all vertices
    parent = [-1] * V             # -1 indicates no parent yet
    mstSet = [False] * V          # All vertices not yet included in MST
    return key, parent, mstSet

# Test case
V = 4
key, parent, mstSet = initialize_prim(V)
print("key =", key)
print("parent =", parent)
print("mstSet =", mstSet)
