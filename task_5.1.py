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

def initialize_prims_arrays(V):
    key = [float('inf')] * V
    parent = [-1] * V
    mstSet = [False] * V
    
    return key, parent, mstSet

V = 4
key, parent, mstSet = initialize_prims_arrays(V)

print(f"For V = {V} vertices:")
print(f"key = {key}")
print(f"parent = {parent}")
print(f"mstSet = {mstSet}")

print("\nVerification:")
print(f"All keys are infinity: {all(k == float('inf') for k in key)}")
print(f"All parents are -1: {all(p == -1 for p in parent)}")
print(f"All mstSet are False: {all(m == False for m in mstSet)}")

V2 = 6
key2, parent2, mstSet2 = initialize_prims_arrays(V2)
print(f"\nFor V = {V2} vertices:")
print(f"key = {key2}")
print(f"parent = {parent2}")
print(f"mstSet = {mstSet2}")
